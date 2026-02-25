#!/usr/bin/env python3
"""Codex notify hook for Trellis.

Codex invokes this command after each completed turn and appends a JSON payload
as the last argv item. We convert that payload + Trellis metadata into a
lightweight snapshot file that Codex skills can reference.
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MAX_SECTION_CHARS = 6000


def parse_payload(argv: list[str]) -> dict[str, Any]:
    if len(argv) < 2:
        return {}

    raw = argv[-1]
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return {}

    if not isinstance(parsed, dict):
        return {}

    return parsed


def read_text(path: Path, fallback: str = "") -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, PermissionError, OSError):
        return fallback


def clip(value: str, max_chars: int = MAX_SECTION_CHARS) -> str:
    value = value.strip()
    if len(value) <= max_chars:
        return value
    return value[: max_chars - 20] + "\n... [truncated]"


def run_context_script(script_path: Path, cwd: Path) -> str:
    if not script_path.is_file():
        return ""

    try:
        result = subprocess.run(
            [sys.executable, "-W", "ignore", str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=8,
            cwd=cwd,
        )
    except (subprocess.SubprocessError, OSError):
        return ""

    if result.returncode != 0:
        return ""

    return result.stdout.strip()


def build_snapshot(project_dir: Path, payload: dict[str, Any]) -> str:
    trellis_dir = project_dir / ".trellis"

    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    turn_id = payload.get("turn-id", "unknown")
    thread_id = payload.get("thread-id", "unknown")

    parts: list[str] = []
    parts.append("# Trellis Codex Context Snapshot")
    parts.append("")
    parts.append(f"- GeneratedAt: {generated_at}")
    parts.append(f"- ThreadID: {thread_id}")
    parts.append(f"- TurnID: {turn_id}")

    input_messages = payload.get("input-messages")
    if isinstance(input_messages, list) and input_messages:
        last_user_message = str(input_messages[-1]).strip()
        if last_user_message:
            parts.append("- LastUserMessage:")
            parts.append(f"  {last_user_message}")

    last_assistant_message = payload.get("last-assistant-message")
    if isinstance(last_assistant_message, str) and last_assistant_message.strip():
        parts.append("- LastAssistantMessage:")
        parts.append(f"  {last_assistant_message.strip()}")

    parts.append("")
    parts.append("## Current State")

    current_state = run_context_script(trellis_dir / "scripts" / "get_context.py", project_dir)
    if current_state:
        parts.append("```")
        parts.append(clip(current_state))
        parts.append("```")
    else:
        parts.append("No get_context.py output available.")

    parts.append("")
    parts.append("## Workflow")
    workflow = read_text(trellis_dir / "workflow.md", "workflow.md not found")
    parts.append("```")
    parts.append(clip(workflow))
    parts.append("```")

    parts.append("")
    parts.append("## Spec Index")
    for label, rel in (
        ("Frontend", "spec/frontend/index.md"),
        ("Backend", "spec/backend/index.md"),
        ("Guides", "spec/guides/index.md"),
    ):
        parts.append(f"### {label}")
        content = read_text(trellis_dir / rel, f"{rel} not found")
        parts.append("```")
        parts.append(clip(content, 3000))
        parts.append("```")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def write_snapshot(project_dir: Path, payload: dict[str, Any]) -> None:
    context_dir = project_dir / ".codex" / "context"
    context_dir.mkdir(parents=True, exist_ok=True)

    snapshot_path = context_dir / "trellis-context.md"
    event_path = context_dir / "last-notify-event.json"

    snapshot_path.write_text(build_snapshot(project_dir, payload), encoding="utf-8")
    event_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    payload = parse_payload(sys.argv)

    cwd_value = payload.get("cwd")
    if isinstance(cwd_value, str) and cwd_value.strip():
        project_dir = Path(cwd_value).resolve()
    else:
        project_dir = Path.cwd().resolve()

    # Hook should never block Codex usage.
    try:
        if (project_dir / ".trellis").is_dir():
            write_snapshot(project_dir, payload)
    except OSError:
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
