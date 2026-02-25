import path from "node:path";
import {
  getAllHooks,
  getAllSkills,
  getConfigTemplate,
} from "../templates/codex/index.js";
import { ensureDir, writeFile } from "../utils/file-writer.js";
import { resolvePlaceholders } from "./shared.js";

/**
 * Configure Codex by writing skill templates.
 *
 * Output:
 * - .agents/skills/<skill-name>/SKILL.md
 * - .codex/hooks/*
 * - .codex/config.toml
 */
export async function configureCodex(cwd: string): Promise<void> {
  const skillsRoot = path.join(cwd, ".agents", "skills");
  ensureDir(skillsRoot);

  for (const skill of getAllSkills()) {
    const skillDir = path.join(skillsRoot, skill.name);
    ensureDir(skillDir);
    const targetPath = path.join(skillDir, "SKILL.md");
    await writeFile(targetPath, skill.content);
  }

  const codexRoot = path.join(cwd, ".codex");
  ensureDir(codexRoot);

  for (const hook of getAllHooks()) {
    const targetPath = path.join(codexRoot, hook.targetPath);
    ensureDir(path.dirname(targetPath));
    await writeFile(targetPath, hook.content);
  }

  const config = getConfigTemplate();
  await writeFile(
    path.join(codexRoot, config.targetPath),
    resolvePlaceholders(config.content),
  );
}
