/**
 * Codex templates
 *
 * These are GENERIC templates for user projects.
 * Do NOT use Trellis project's own .agents/skills or .codex directory (which may be customized).
 *
 * Directory structure:
 *   codex/
 *   ├── config.toml
 *   ├── hooks/
 *   │   └── notify.py
 *   └── skills/
 *       └── <skill-name>/
 *           └── SKILL.md
 */

import { readdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

function readTemplate(relativePath: string): string {
  return readFileSync(join(__dirname, relativePath), "utf-8");
}

function listFiles(dir: string): string[] {
  try {
    return readdirSync(join(__dirname, dir));
  } catch {
    return [];
  }
}

function listSkillNames(): string[] {
  try {
    return readdirSync(join(__dirname, "skills"), { withFileTypes: true })
      .filter((entry) => entry.isDirectory())
      .map((entry) => entry.name)
      .sort();
  } catch {
    return [];
  }
}

export interface SkillTemplate {
  name: string;
  content: string;
}

export interface HookTemplate {
  targetPath: string;
  content: string;
}

export function getAllSkills(): SkillTemplate[] {
  const skills: SkillTemplate[] = [];

  for (const name of listSkillNames()) {
    const content = readTemplate(`skills/${name}/SKILL.md`);
    skills.push({ name, content });
  }

  return skills;
}

export function getAllHooks(): HookTemplate[] {
  const hooks: HookTemplate[] = [];

  for (const file of listFiles("hooks")) {
    const content = readTemplate(`hooks/${file}`);
    hooks.push({ targetPath: `hooks/${file}`, content });
  }

  return hooks;
}

export function getConfigTemplate(): HookTemplate {
  return {
    targetPath: "config.toml",
    content: readTemplate("config.toml"),
  };
}
