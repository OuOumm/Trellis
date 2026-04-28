<p align="center">
<picture>
<source srcset="assets/trellis.png" media="(prefers-color-scheme: dark)">
<source srcset="assets/trellis.png" media="(prefers-color-scheme: light)">
<img src="assets/trellis.png" alt="Trellis Logo" width="500" style="image-rendering: -webkit-optimize-contrast; image-rendering: crisp-edges;">
</picture>
</p>

<p align="center">
<strong>Make AI coding reliable at team scale.</strong><br/>
<sub>A repo-native operating layer for specs, tasks, workflows, checks, and memory across Claude Code, Cursor, Codex, OpenCode, and more.</sub>
</p>

<p align="center">
<a href="./README_CN.md">简体中文</a> •
<a href="https://docs.trytrellis.app/">Docs</a> •
<a href="https://docs.trytrellis.app/guide/ch02-quick-start">Quick Start</a> •
<a href="https://docs.trytrellis.app/guide/ch13-multi-platform">Supported Platforms</a> •
<a href="https://docs.trytrellis.app/guide/ch08-real-world">Use Cases</a>
</p>

<p align="center">
<a href="https://www.npmjs.com/package/@mindfoldhq/trellis"><img src="https://img.shields.io/npm/v/@mindfoldhq/trellis.svg?style=flat-square&color=2563eb" alt="npm version" /></a>
<a href="https://www.npmjs.com/package/@mindfoldhq/trellis"><img src="https://img.shields.io/npm/dw/@mindfoldhq/trellis?style=flat-square&color=cb3837&label=downloads" alt="npm downloads" /></a>
<a href="https://github.com/mindfold-ai/Trellis/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-16a34a.svg?style=flat-square" alt="license" /></a>
<a href="https://github.com/mindfold-ai/Trellis/stargazers"><img src="https://img.shields.io/github/stars/mindfold-ai/Trellis?style=flat-square&color=eab308" alt="stars" /></a>
<a href="https://docs.trytrellis.app/"><img src="https://img.shields.io/badge/docs-trytrellis.app-0f766e?style=flat-square" alt="docs" /></a>
<a href="https://discord.com/invite/tWcCZ3aRHc"><img src="https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord" /></a>
<a href="https://github.com/mindfold-ai/Trellis/issues"><img src="https://img.shields.io/github/issues/mindfold-ai/Trellis?style=flat-square&color=e67e22" alt="open issues" /></a>
<a href="https://github.com/mindfold-ai/Trellis/pulls"><img src="https://img.shields.io/github/issues-pr/mindfold-ai/Trellis?style=flat-square&color=9b59b6" alt="open PRs" /></a>
<a href="https://deepwiki.com/mindfold-ai/Trellis"><img src="https://img.shields.io/badge/Ask-DeepWiki-blue?style=flat-square" alt="Ask DeepWiki" /></a>
<a href="https://chatgpt.com/?q=Explain+the+project+mindfold-ai/Trellis+on+GitHub"><img src="https://img.shields.io/badge/Ask-ChatGPT-74aa9c?style=flat-square&logo=openai&logoColor=white" alt="Ask ChatGPT" /></a>
</p>

<p align="center">
<img src="assets/trellis-demo.gif" alt="Trellis workflow demo" width="100%">
</p>

## Proven beyond solo workflows

Most AI coding frameworks stop at personal productivity. Trellis is already used by individual builders, open-source maintainers, teams inside tech giants, labs at top universities, and software engineering departments at public companies.

That matters because Trellis is battle-tested where AI coding usually breaks: production projects with hundreds of thousands of lines of code, monorepos, multi-person teams, shared standards, task boundaries, reviewability, memory, and a rollout path that does not depend on every developer using the same IDE.

## AI coding is no longer a solo prompt problem

One developer can usually keep a coding agent on track with enough prompting. A team cannot.

Once multiple people use Claude Code, Cursor, Codex, OpenCode, or another agent in the same repository, the hard problems change:

| What breaks               | What it looks like                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Context drifts**        | Every session starts from a different version of "how this codebase works."                |
| **Standards stay verbal** | Team conventions live in chat history, review comments, or one senior engineer's head.     |
| **Tasks sprawl**          | Agents follow nearby context, modify adjacent modules, and make PRs harder to review.      |
| **Knowledge disappears**  | A bug, workaround, or architecture rule is discovered once, then lost in a transcript.     |
| **Tools fragment**        | Half the team uses one AI tool, another half uses a different one, and the workflow forks. |

Trellis turns those loose instructions into a versioned project system. Your repository becomes the source of truth for how AI agents should plan, build, check, and remember work.

## What Trellis gives you

| Layer                     | What it does                                                                                           | Why it matters                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **Specs**                 | Store engineering standards in `.trellis/spec/` and inject the relevant ones automatically.            | Agents stop guessing your conventions and reviewers stop repeating the same comments. |
| **Tasks**                 | Keep PRDs, acceptance criteria, implementation context, review notes, and status in `.trellis/tasks/`. | Every AI session has a clear boundary and a reviewable reason for the change.         |
| **Workflow**              | Give agents shared commands for brainstorm, pre-dev context, checks, finish gates, and spec updates.   | Your team gets a repeatable process instead of one-off prompt recipes.                |
| **Workspace memory**      | Preserve per-developer session journals in `.trellis/workspace/`.                                      | New sessions resume with real project context instead of an empty chat window.        |
| **Multi-agent execution** | Run isolated agents in git worktrees for independent tasks.                                            | Parallel AI work stops turning one branch into a conflict magnet.                     |
| **Multi-platform wiring** | Generate the right files for Claude Code, Cursor, Codex, OpenCode, iFlow, Kiro, Gemini CLI, and more.  | The workflow stays in the repo even when the team changes tools.                      |

## Why teams choose Trellis

Trellis is not trying to be another coding agent. It is the coordination layer around the agents you already use.

It is built for teams that want AI coding to behave like engineering work:

- **Repo-native by default**: specs, tasks, workflows, and memory live beside the code and can be reviewed like code.
- **Brownfield-friendly**: Trellis works with existing projects, old decisions, and real codebases where context matters.
- **Team-shareable**: one person's hard-won rule can become a shared spec that every future session reads.
- **Platform-portable**: Claude Code, Cursor, Codex, OpenCode, and other tools can share the same `.trellis/` source of truth.
- **Enterprise-ready shape**: teams can pilot it in one repo, standardize specs, then roll the workflow across departments without locking into one IDE.

## Quick Start

### Prerequisites

- **Node.js** >= 18
- **Python** >= 3.10, required for hooks and automation scripts

### Install

```bash
npm install -g @mindfoldhq/trellis@latest
```

### Initialize a repository

```bash
# Start Trellis and create a developer workspace
trellis init -u your-name

# Or configure the AI tools you already use
trellis init --claude --cursor --codex --opencode -u your-name
```

`-u your-name` creates `.trellis/workspace/your-name/` for your session journal and personal continuity.

Platform flags can be mixed and matched:

```bash
trellis init --claude --cursor --opencode --iflow --codex --kilo --kiro --gemini
trellis init --antigravity --windsurf --qoder --codebuddy --copilot --droid
```

See the [Supported Platforms](https://docs.trytrellis.app/guide/ch13-multi-platform) guide for per-tool setup details.

## Your first Trellis workflow

Command names are exposed as slash commands, skills, workflows, prompts, or hooks depending on the AI platform. The core workflow is the same:

| Step | Command           | Use it when                                                                                                                   |
| ---- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1    | `/start`          | Load project context, active tasks, specs, and recent journal entries. On hook-enabled platforms, this can run automatically. |
| 2    | `/brainstorm`     | Turn a rough request into a PRD with scope, decisions, risks, and acceptance criteria.                                        |
| 3    | `/before-dev`     | Load the specific development guidelines needed for the task before writing code.                                             |
| 4    | Build             | Let the agent implement against the PRD and injected specs.                                                                   |
| 5    | `/check`          | Review changes against project specs and fix violations before handoff.                                                       |
| 6    | `/finish-work`    | Run the pre-commit gate: lint, typecheck, tests, docs impact, migrations, and API checks.                                     |
| 7    | `/update-spec`    | Capture new conventions or repeated review feedback into `.trellis/spec/`.                                                    |
| 8    | `/record-session` | Save what changed, what was tested, and what remains into your workspace journal.                                             |

For larger tasks, use `/parallel` to plan and run multiple worktree agents in isolation.

## How it works

Trellis keeps the durable workflow in `.trellis/` and generates platform-specific entry points around it.

```text
.trellis/
├── spec/                    # Project standards, patterns, and guides
├── tasks/                   # Task PRDs, context files, and status
├── workspace/               # Developer journals and session continuity
├── workflow.md              # Shared workflow contract
└── scripts/                 # Automation that powers hooks and commands
```

Depending on the platforms you enable, Trellis also creates integration files such as:

```text
.claude/                    # Claude Code commands, hooks, agents
.cursor/                    # Cursor commands and rules
AGENTS.md                   # Agent-compatible project instructions
.agents/                    # Shared project skills
.codex/                     # Codex config, hooks, skills, agents
.opencode/                  # OpenCode integration
.iflow/                     # iFlow commands, hooks, agents
.kilocode/                  # Kilo workflows
.kiro/skills/               # Kiro skills
.gemini/                    # Gemini CLI commands
.agent/workflows/           # Antigravity workflows
.windsurf/workflows/        # Windsurf workflows
.qoder/                     # Qoder skills
.codebuddy/                 # CodeBuddy commands
.github/copilot/            # GitHub Copilot prompts
.github/hooks/              # GitHub Copilot hooks
.github/prompts/            # GitHub prompt files
.factory/                   # Factory Droid commands
```

At a high level:

1. Put durable team knowledge in `.trellis/spec/`.
2. Start work from a task PRD in `.trellis/tasks/`.
3. Let Trellis inject only the relevant context for the current step.
4. Run checks before handoff.
5. Record what happened and promote reusable lessons back into specs.

## Where Trellis fits

| If you are using...                         | Trellis adds...                                                                             |
| ------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `CLAUDE.md`, `AGENTS.md`, or `.cursorrules` | Structure, task context, scoped spec injection, memory, and platform-aware workflow wiring. |
| Claude Code, Cursor, Codex, or OpenCode     | A shared repo-level process that survives tool changes.                                     |
| Spec-driven tools                           | Brownfield task flow, team memory, checks, journals, and multi-platform integration.        |
| Role or skill packs                         | A durable project system that stores standards and decisions in version control.            |
| Manual PR review                            | A way to turn repeated review feedback into executable AI context.                          |

Trellis is a good fit when AI coding is already useful but not yet predictable enough for a team.

It may be too much if you only need a single agent for a small throwaway prototype.

## Use cases

### "AI keeps ignoring our conventions"

Write a rule once in `.trellis/spec/`, then let Trellis inject it into the right sessions. The rule becomes part of the repository instead of another instruction pasted into chat.

### "We need consistent AI work across a team"

Use shared specs and task PRDs so every developer and agent works from the same project facts. Personal journals stay separate; team standards stay reviewable.

### "Our agents make PRs too large"

Start from tasks with explicit goals, non-goals, and acceptance criteria. Trellis gives the agent a boundary before implementation starts.

### "We need multiple agents without branch chaos"

Run `/parallel` to split independent work into git worktrees. Each agent gets its own branch, context, and task directory.

### "The team is split across AI tools"

Initialize the platforms each person uses. Trellis keeps the workflow in `.trellis/`, then generates the right command, skill, hook, or workflow files for each tool.

## Spec Templates & Marketplace

Specs ship as editable templates. They are meant to be customized for your stack, architecture, and review standards.

You can start from scratch or fetch templates from a custom registry:

```bash
trellis init --registry https://github.com/your-org/your-spec-templates
```

Browse available templates and learn how to publish your own on the [Spec Templates page](https://docs.trytrellis.app/templates/specs-index).

## What's New

- **v0.4.0**: command consolidation (`before-backend-dev` + `before-frontend-dev` -> `before-dev`, `check-backend` + `check-frontend` -> `check`), new `/update-spec` command for capturing knowledge into specs, internal Python scripts refactoring.
- **v0.3.6**: task lifecycle hooks, custom template registries (`--registry`), parent-child subtasks, fix PreToolUse hook for Claude Code v2.1.63+.
- **v0.3.5**: hotfix for delete migration manifest field name in Kilo workflows.
- **v0.3.4**: Qoder platform support, Kilo workflows migration, record-session task awareness.
- **v0.3.1**: background watch mode for `trellis update`, improved `.gitignore` handling, docs refresh.
- **v0.3.0**: platform support expanded from 2 to 10, Windows compatibility, remote spec templates, `/trellis:brainstorm`.

See the [changelog](https://docs.trytrellis.app/changelog/v0.4.0) for release details.

## FAQ

<details>
<summary><strong>How is Trellis different from <code>CLAUDE.md</code>, <code>AGENTS.md</code>, or <code>.cursorrules</code>?</strong></summary>

Those files are useful entry points, but they tend to become monolithic. Trellis adds a structured project system around them: scoped specs, task PRDs, workflow gates, workspace memory, and platform-aware generated files.

</details>

<details>
<summary><strong>Is Trellis only for Claude Code?</strong></summary>

No. Trellis supports Claude Code, Cursor, OpenCode, iFlow, Codex, Kilo, Kiro, Gemini CLI, Antigravity, Windsurf, Qoder, CodeBuddy, GitHub Copilot, and Factory Droid.

</details>

<details>
<summary><strong>Do I have to write every spec file manually?</strong></summary>

No. Many teams let AI draft the first version from an existing codebase, then tighten the important rules by hand. Trellis works best when specs stay concrete, short, and reviewable.

</details>

<details>
<summary><strong>Can a team use Trellis without constant merge conflicts?</strong></summary>

Yes. Shared specs and tasks live in the repo. Personal journals live under `.trellis/workspace/{name}/`, so developers keep continuity without overwriting each other.

</details>

<details>
<summary><strong>Is Trellis for solo developers or teams?</strong></summary>

Both. Solo developers use it for memory, conventions, and repeatable workflow. Teams get the larger benefit: shared standards, task boundaries, reviewable context, and platform portability.

</details>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=mindfold-ai/Trellis&type=Date)](https://star-history.com/#mindfold-ai/Trellis&Date)

## Community & Resources

- [Official Docs](https://docs.trytrellis.app/) - Product docs, setup guides, and architecture
- [Quick Start](https://docs.trytrellis.app/guide/ch02-quick-start) - Get Trellis running in a repo fast
- [Supported Platforms](https://docs.trytrellis.app/guide/ch13-multi-platform) - Platform-specific setup and command details
- [Real-World Scenarios](https://docs.trytrellis.app/guide/ch08-real-world) - See how the workflow plays out in practice
- [Changelog](https://docs.trytrellis.app/changelog/v0.4.0) - Track current releases and updates
- [Tech Blog](https://docs.trytrellis.app/blog) - Product thinking and technical writeups
- [GitHub Issues](https://github.com/mindfold-ai/Trellis/issues) - Report bugs or request features
- [Discord](https://discord.com/invite/tWcCZ3aRHc) - Join the community

<p align="center">
<a href="https://github.com/mindfold-ai/Trellis">Official Repository</a> •
<a href="https://github.com/mindfold-ai/Trellis/blob/main/LICENSE">AGPL-3.0 License</a> •
Built by <a href="https://github.com/mindfold-ai">Mindfold</a>
</p>
