# Trellis Docs Deep Research: Harness Framework Documentation Patterns

Date: 2026-04-27
Research focus: what Trellis can borrow from other AI coding harness / spec-driven / agent workflow documentation.

## Executive Summary

Trellis should stop presenting itself mainly as a CLI toolkit and start presenting itself as a repo-native operating layer for team-scale AI coding. The strongest external docs do three things well:

1. They route users by intent before explaining internals.
2. They show a full workflow outcome before listing reference material.
3. They make trust explicit: when to use it, when not to use it, what artifacts are created, how teams roll it out, and how failures are handled.

Trellis already has the harder substance: repo-native specs, task boundaries, workspace memory, multi-platform wiring, hooks, skills, sub-agents, and real enterprise/team adoption. The docs do not yet make that maturity obvious. The current public docs still read closer to "install this framework and learn its commands" than "this is how a team makes AI coding predictable across people, tools, and sessions."

The biggest opportunity is a documentation re-architecture around four entry paths:

- Solo/power user: "Get one useful task done in 10 minutes."
- Team lead: "Roll out Trellis to one repo, then a department."
- Enterprise/platform lead: "Standardize AI coding without locking everyone into one IDE."
- Advanced integrator: "Customize hooks, skills, platforms, templates, and multi-agent workflows."

This matches both external docs patterns and the user research: users value standards, certainty, team coordination, context continuity, and low-friction adoption; they are also blocked by docs, learning cost, fast-changing versions, and workflow heaviness.

## Trellis Context Signals

### Current external posture

The GitHub README now has the right high-level narrative: "Make AI coding reliable at team scale" and "repo-native operating layer." It also highlights that Trellis is not another coding agent, but a coordination layer around existing agents.

The docs site is weaker than the README:

- Homepage says "All-in-one AI framework & toolkit" and "training wheels for AI coding assistants." That undersells the product and makes it sound beginner-oriented.
- The nav is thin at the top: Start Here has only `Trellis`, `Install & First Task`, and `Commands, Tasks & Specs`; there is only one named use case.
- Several public routes appear to overlap: `/quickstart`, `/guide/ch02-quick-start`, `/release/guide/ch02-quick-start`, `/start/install-and-first-task`.
- Some copy looks generated or broken in rendered output, e.g. repeated "OpenAI Open in ChatGPT."
- Version messaging is confusing: beta/release banners, install commands, and Python requirements are not consistently aligned with README.

### User research signals that should drive docs

From the interview and survey materials:

- The strongest validated value is not "AI coding" in general, but making AI work follow shared standards and context.
- Users choose Trellis for "规范/约束", team collaboration, lower repeated explanation cost, and context/memory.
- Nearly 30% of survey respondents mention docs, tutorials, onboarding, or learning cost as a blocker.
- "Too heavy vs not heavy enough" splits along solo vs team/enterprise usage. This means docs need explicit paths, not one default mental model.
- Superpower / Superpowers conflict and confusion is a recurring user issue. Trellis needs a troubleshooting and comparison page for harness coexistence.
- Team and enterprise users need rollout guidance, success metrics, and confidence that Trellis protects existing configuration and scales across platforms.
- Stable users need a "stable vs beta" story and a clear update/migration path.

## External Documentation Patterns

### GitHub Spec Kit

Useful patterns:

- Opens with philosophy and development phases rather than command lists.
- Makes the SDD promise explicit: specs define intent before implementation.
- Names target scenarios: greenfield, creative exploration, brownfield modernization, enterprise constraints, user-centric development.
- Gives credibility through "experimental goals" instead of pretending every path is equally mature.

What Trellis should borrow:

- A visible "development phases" model, but adapted to Trellis: Discover context -> Plan task -> Inject specs -> Implement -> Check -> Capture memory.
- A clear "enterprise constraints" section: design systems, compliance, shared standards, review gates, and platform heterogeneity.
- A "where Trellis is strong / where it is not" page to avoid overclaiming.

What Trellis should not copy:

- The "specifications are executable" framing is too strong for Trellis. Trellis should say "specs are injected, versioned, and reviewable; AI still needs checks."
- Avoid a waterfall impression. Trellis' advantage is durable context plus iterative workflow, not ceremony.

### OpenSpec

Useful patterns:

- Homepage immediately explains "why", then shows a concrete example workflow.
- The workflow transcript is short and memorable: create change -> generate planning docs -> implement -> archive.
- It has audience segmentation: individual developers, teams/code review, brownfield codebases, tool-agnostic users.
- It has explicit comparison pages against Spec Kit, BMAD, Kiro, and "nothing."
- It has guides/resources for search and skimming: what SDD is, best practices, use cases, glossary, setup by tool.

What Trellis should borrow:

- Add a compact "See Trellis in action" transcript that shows exact files created and where the human reviews.
- Add a "Who Trellis is for" block with separate solo, team, brownfield, enterprise, and multi-platform paths.
- Add a comparison section, but keep it factual and less combative than OpenSpec.
- Add a glossary for terms like spec, task, workspace, workflow, hook, skill, sub-agent, JSONL, journal, marketplace, registry.

What Trellis can beat:

- OpenSpec positions itself as lightweight SDD. Trellis can own the larger team-operating-layer story: cross-session memory, platform portability, quality gates, hooks, multi-agent worktrees, templates, and enterprise rollout.

### Kiro

Useful patterns:

- Docs start from core capabilities: Specs, Hooks, Agentic chat, Steering, MCP, Privacy.
- Feature Specs page has "when to use" and "not ideal for" sections.
- It supports workflow variants: requirements-first and design-first.
- It uses structured requirement syntax examples, making abstract planning concrete.
- Steering docs explain scope, team steering, foundational files, inclusion modes, file references, and best practices.

What Trellis should borrow:

- Every major Trellis capability page should include "best for" and "not ideal for."
- Add workflow variants:
  - Requirements-first: rough request -> brainstorm/PRD -> implementation.
  - Existing-code-first: bootstrap specs -> task plan -> implementation.
  - Fix-first: bug report -> repro/check -> minimal patch -> spec update.
  - Team rollout: pilot repo -> shared specs -> review gate -> expand.
- Add a "Trellis spec writing patterns" page with concrete before/after examples and testable wording.
- Add "scope and inclusion" docs for Trellis specs, similar to Kiro steering inclusion modes, but grounded in Trellis JSONL/spec indexes.

### BMad Method

Useful patterns:

- It uses a Diataxis-like structure: Tutorials, How-To Guides, Explanation, Reference.
- It explicitly tells new users where to start and gives a guided helper path.
- It has a workflow map, which is exactly what complex AI workflows need.
- It treats customization as a top-level path, not hidden reference material.

What Trellis should borrow:

- Rebuild docs nav around Tutorials / Guides / Concepts / Reference.
- Add a visual workflow map as a primary page.
- Make `/start` / `continue` / bootstrap-guided onboarding the default beginner story.
- Keep customization visible but below the beginner/team rollout paths.

### Agent OS

Useful patterns:

- The documentation is clear about strategic scope: Agent OS v3 focuses on discovering, documenting, and injecting development standards rather than replacing native AI tool capabilities.
- It explains a two-tier model: base installation vs project installation.
- It names a small command set around standards discovery, indexing, injection, spec shaping, and product planning.
- It emphasizes "works alongside modern AI coding tools rather than replace them."

What Trellis should borrow:

- Tighten Trellis' own "we do not replace your agent" message. The README already does this; docs should match it.
- Explain the source-of-truth model explicitly: `.trellis/` is durable, platform folders are generated adapters.
- Add a "standards discovery and injection" conceptual page, because that is one of Trellis' strongest enterprise messages.

### Superpowers

Useful patterns:

- Marketplace page is concise: what it teaches Claude, the core methodologies, and exact slash commands to use.
- It uses social proof through install count and platform placement.
- It makes methodology concrete: TDD, debugging, brainstorming, execute-plan, review checkpoints.

What Trellis should borrow:

- Add a skills catalog by job-to-be-done: Brainstorm, Before Dev, Check, Finish, Update Spec, Record Session, Break Loop, Parallel.
- For each skill, show: when it triggers, what it reads, what it writes, and when to invoke manually.
- Add trust proof. Trellis can use adoption patterns, sanitized enterprise rollout stories, star/download data, and real case studies.

### SuperClaude

Useful patterns:

- Large command set is grouped by question: orchestration, discovery, implementation, quality, improvement, documentation.
- Has enterprise workflow recipes chaining multiple commands.
- Shows MCP/tool routing and memory/repo indexing as part of the workflow.

What Trellis should borrow:

- Group commands by lifecycle question, not alphabetically.
- Provide 3-5 canonical workflow recipes:
  - New feature in brownfield app.
  - Team rollout into existing repo.
  - Multi-agent worktree execution.
  - Fix repeated review feedback by updating spec.
  - Cross-platform team setup.

What Trellis should avoid:

- Do not lead with a giant command surface. User research already says extra actions can become mental burden.

## What Trellis Docs Should Become

### Recommended positioning

Current docs positioning to avoid:

- "Training wheels for AI coding assistants"
- "All-in-one AI framework & toolkit"

Recommended positioning:

> Trellis is a repo-native operating layer that makes AI coding reliable across teams, tools, and sessions.

Supporting copy:

> It turns engineering standards, task boundaries, workflow gates, and session memory into versioned project files. Your team can keep using Claude Code, Cursor, Codex, OpenCode, Kiro, Gemini, or other agents while sharing the same source of truth.

### Recommended information architecture

#### Start Here

1. What is Trellis?
2. Choose Your Path
3. Install & First Task
4. Bootstrap Specs from an Existing Repo
5. Upgrade from CLAUDE.md / AGENTS.md / Cursor Rules

#### Core Concepts

1. Concept Map: Specs, Tasks, Workspace, Workflow
2. Specs: Standards AI Actually Follows
3. Tasks & PRDs: Boundaries for AI Work
4. Workspace Memory: Explicit Journaling, Not Magic Memory
5. Workflow Lifecycle: Plan, Build, Check, Finish, Learn
6. Platform Adapters: Claude, Cursor, Codex, OpenCode, Kiro, Kilo, Gemini, etc.
7. Hooks, Skills, Sub-agents, Commands

#### Guides

1. Write Better Specs
2. Team Rollout Playbook
3. Brownfield / Monorepo Adoption
4. Multi-agent Worktrees
5. Enterprise Deployment and Governance
6. Troubleshooting and Known Conflicts
7. Updating and Migrations

#### Use Cases

1. Make AI Follow Team Conventions
2. Reduce Repeated PR Review Feedback
3. Run AI Coding Across Multiple IDEs
4. Onboard a 50-person Department
5. Manage Large Brownfield Repos
6. Coordinate Parallel Agents Safely

#### Reference

1. CLI Commands
2. Platform Matrix
3. File Structure
4. JSONL Context Config
5. task.json Schema
6. Hook Reference
7. Skill Reference
8. Template Registry Reference

#### Community / Marketplace

1. Spec Templates
2. Skills
3. Showcase
4. Contributing
5. Changelog

## Priority Backlog

### P0: Fix trust-breaking docs issues

- Pick canonical routes and redirect duplicates.
- Align release/beta versioning, install commands, supported platforms, and Python requirements.
- Remove duplicated render artifacts such as "OpenAI Open in ChatGPT."
- Make README and docs positioning consistent.

### P0: Add "Choose Your Path"

This should be the first major onboarding page. It should ask:

- Are you trying Trellis alone?
- Are you rolling it out to a team?
- Are you adding it to a large existing repo?
- Are you standardizing across multiple AI tools?
- Are you extending Trellis?

Each path should end with 2-4 next links, not a full platform matrix.

### P0: Rewrite first-task onboarding

The first-task guide should show a complete outcome:

1. Install.
2. Init.
3. Bootstrap or write one spec.
4. Ask for a real task.
5. See the task directory and PRD.
6. See which specs get injected.
7. Run check/finish.
8. See the journal entry.

This should be a concrete artifact story, not a list of flags.

### P0: Add "Write Specs AI Actually Follows"

This is the page most directly tied to user pain. Include:

- Bad vs good examples.
- How specific is specific enough.
- How long a spec should be.
- How to split specs.
- How to include paths and code examples.
- How to prevent spec bloat.
- How to test if a spec works.

### P1: Publish Team Rollout Playbook

Use the enterprise landing doc as source material. Structure:

1. Pilot repo selection.
2. Bootstrap first specs.
3. Run one full task.
4. Establish review/check gates.
5. Promote repeated review feedback into specs.
6. Add more platforms and team members.
7. Measure success.

Success metrics can include:

- Fewer repeated review comments.
- More consistent AI output.
- Faster new-member onboarding.
- Less task scope sprawl.
- Better PRD clarity.
- Multi-platform usage without workflow fragmentation.

### P1: Add Comparisons and Migration

Comparison pages should be factual and user-helpful:

- Trellis vs CLAUDE.md / AGENTS.md / Cursor Rules.
- Trellis vs Superpowers.
- Trellis vs OpenSpec.
- Trellis vs GitHub Spec Kit.
- Trellis vs BMad / Agent OS.
- Trellis with Kiro / Cursor / Codex / OpenCode.

Include "use both when..." and "migrate when..." rather than pure competitor framing.

### P1: Add Troubleshooting and Harness Collision Docs

Known pages needed:

- Superpowers / Superpower conflict detection and what to do.
- Specs not being followed.
- Context too long.
- Existing settings overwritten or protected.
- Hook did not fire.
- Codex / Claude / Cursor platform differences.
- Update/migration safety.
- How to verify Trellis is active.

### P1: Add Case Studies and Enterprise Proof

Trellis has stronger social proof than the docs show. Add sanitized stories:

- Enterprise department rollout.
- Brownfield monorepo.
- Multi-platform team.
- Research/lab environment.
- Game or large-repo workflow, once validated for public use.

Each case study should include:

- Starting pain.
- Setup.
- Workflow.
- Outcome.
- What changed in specs/tasks/review.

### P2: Add glossary and command lifecycle map

The docs currently define many terms, but the mental model should be more scannable. A glossary and lifecycle map will reduce new-user overload.

## Recommended Homepage Outline

First viewport:

- H1: Make AI coding reliable at team scale.
- Subcopy: Repo-native specs, tasks, workflow gates, and memory for Claude Code, Cursor, Codex, OpenCode, Kiro, Gemini, and more.
- CTAs: Start in 10 minutes / Team rollout guide / GitHub.
- Trust strip: stars, npm downloads, supported platforms, enterprise/team adoption statement.

Problem section:

- AI coding works for one person. Teams need shared context, task boundaries, review gates, and memory.

How Trellis works:

- Specs: standards.
- Tasks: boundaries.
- Workflow: gates.
- Workspace: continuity.
- Platform adapters: portability.

See it in action:

- A short transcript that creates a task, generates PRD, injects specs, implements, checks, updates spec, records session.

Choose your path:

- Solo builder.
- Team lead.
- Enterprise/platform lead.
- Advanced customizer.

Proof:

- Sanitized enterprise usage.
- Team adoption notes.
- Marketplace/templates.
- Community.

## Source List

External:

- Trellis docs: https://docs.trytrellis.app/
- Trellis start docs: https://docs.trytrellis.app/start/install-and-first-task
- Trellis concepts: https://docs.trytrellis.app/concepts/overview
- Trellis FAQ: https://docs.trytrellis.app/guides/faq
- GitHub Spec Kit docs: https://github.github.io/spec-kit/
- OpenSpec: https://openspec.pro/
- Kiro docs: https://kiro.dev/docs/
- Kiro Feature Specs: https://kiro.dev/docs/specs/feature-specs/
- Kiro Steering: https://kiro.dev/docs/steering/
- BMad Method docs: https://docs.bmad-method.org/
- Superpowers plugin: https://claude.com/plugins/superpowers
- Superpowers GitHub: https://github.com/obra/superpowers
- Agent OS overview: https://deepwiki.com/buildermethods/agent-os/1-agent-os-overview
- SuperClaude command reference: https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/docs/user-guide/commands.md

Internal user/context materials reviewed:

- Cross-user Trellis interview insight summary.
- Full interview wiki index.
- User survey summary.
- Enterprise rollout document.
- Current repository README and local project state.
