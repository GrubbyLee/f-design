<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/f-design-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/f-design-logo-light.svg">
    <img alt="f-design - Frontend Design Orchestration" src="assets/f-design-logo-light.svg" width="560">
  </picture>
</p>

# f-design

English | [简体中文](README.zh-CN.md)

[![Validate](https://github.com/GrubbyLee/f-design/actions/workflows/validate.yml/badge.svg)](https://github.com/GrubbyLee/f-design/actions/workflows/validate.yml)
[![Sync to Gitee](https://github.com/GrubbyLee/f-design/actions/workflows/sync-to-gitee.yml/badge.svg)](https://github.com/GrubbyLee/f-design/actions/workflows/sync-to-gitee.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> A frontend design orchestration skill for Codex, Claude Code, Cursor, Qwen Code, and other AI development environments.

`f-design` is not another UI style preset. It is a frontend control skill: it helps an AI coding agent read product context, choose a design direction, select helper skills, build a v0, implement the UI, and verify the result with screenshots before delivery.

Use it when you want fewer generic AI-looking interfaces and a more disciplined frontend design/development loop.

## What It Does

- Acts as a frontend entry skill and navigator.
- Supports two modes:
  - **Navigation mode**: invoked without a concrete task, it lists the best frontend tasks and helper skills available in the environment.
  - **Execution mode**: invoked with a real task, it follows a structured design-to-implementation workflow.
- Scales the design process from direct fixes to exploratory design, based on uncertainty and the cost of reversing a decision.
- Produces and presents reviewable artifacts such as wireframes, standalone HTML prototypes, reference boards, images, or motion studies when they are needed.
- Automatically opens standalone HTML on a shared local desktop, manages HTTP review servers when needed, and uses host-accessible links or screenshots in remote environments.
- Pauses at explicit confirmation gates so the user can approve, choose a direction, or request changes before expensive implementation.
- Routes tasks such as dashboards, admin panels, landing pages, redesigns, screenshot-to-code work, mobile UI, animation, 3D, and UI reviews.
- Uses project/local preference files without hard-coding personal taste into the public skill.
- Provides reusable scripts for frontend environment detection, artifact presentation, screenshot QA, and syncing the skill across local AIDE directories.

## Quick Start

Install for Codex:

```bash
git clone https://github.com/GrubbyLee/f-design.git ~/.codex/skills/f-design
```

Optional: sync the same skill to Claude Code, Cursor, and Qwen Code local skill directories:

```bash
bash ~/.codex/skills/f-design/scripts/sync-aide.sh
```

The sync script copies the current `f-design` folder to:

```text
~/.claude/skills/f-design
~/.cursor/skills/f-design
~/.qwen/skills/f-design
```

## Invocation

Different AIDE tools use different skill invocation syntax. The portable contract is simple: ask the agent to use `f-design`.

| Environment | Suggested invocation |
|---|---|
| Codex | `use f-design`, `f-design`, `$f-design`, or `@f-design` when supported |
| Claude Code | `/f-design` when installed as a Claude skill, or `use f-design` |
| Cursor | `use f-design`, or point the agent at `SKILL.md` |
| Qwen Code | `use f-design`, or point the agent at `SKILL.md` |
| Other AIDE | Tell the agent to read `SKILL.md` and follow `f-design` |

## Mode 1: Navigation

When you only type:

```text
f-design
```

the agent should not start coding. It should show a compact menu of frontend capabilities and helper skills, for example:

```text
f-design is ready. Pick a frontend task:

1. Build a product screen / dashboard / tool
   Primary: f-design
   Helpers if available: web-design-engineer, webapp-testing

2. Improve visual taste of an existing page
   Primary: f-design
   Helpers if available: design-taste-frontend, web-design-guidelines

3. Add complex animation
   Primary: f-design
   Helpers if available: gsap, animejs

4. Build 3D / WebGL
   Primary: f-design
   Helpers if available: three
```

## Mode 2: Execution

When you provide a real task:

```text
Use f-design to build a creator dashboard for reviewing generated media.
```

the agent should follow this loop:

1. Read product context.
2. Choose Level 0, 1, or 2 design depth.
3. Define the user's job, information priority, structure, states, and success criteria.
4. Select the smallest useful helper capability set.
5. For exploratory work, produce the lowest-cost useful review artifact, open or otherwise present it, and wait for user confirmation.
6. Lock the approved design contract and design system.
7. Build a viewable v0 for substantial work.
8. Complete implementation using the existing stack and conventions.
9. Run screenshot QA on desktop, tablet, and mobile.
10. Enforce no-ship gates before claiming completion.

Confirmation is proportional, not automatic. Isolated fixes and clearly directed work can continue without interruption. New products, major redesigns, workflow changes, brand-defining pages, or artifacts explicitly presented for review require approval before full implementation. Creating a file is not presentation: the user must receive an opened browser view, attached media, or an immediately usable absolute link or URL.

## Preference Files

`f-design` keeps open-source defaults separate from personal or project preferences.

Lookup order:

```text
1. .f-design/profile.md in the current project
2. ~/.f-design/preferences.md on the local machine
3. references/design-defaults.md bundled with this skill
```

Templates:

```text
references/project-profile.example.md
references/local-overrides.example.md
```

Do not commit private names, paths, API keys, or personal taste to the public skill.

## Scripts

Detect a frontend environment:

```bash
bash scripts/detect-frontend-env.sh .
```

Capture desktop/tablet/mobile screenshots:

```bash
python3 scripts/capture-audit.py http://localhost:3000 --out .codex/frontend-audit
```

Open one or more standalone HTML review artifacts and return immediately:

```bash
python3 scripts/present-design.py open \
  ".codex/design/<design-id>/direction-a.html" \
  ".codex/design/<design-id>/direction-b.html"
```

Start, inspect, and stop a managed background server when HTTP is required:

```bash
python3 scripts/present-design.py serve ".codex/design/<design-id>/prototype.html"
python3 scripts/present-design.py status
python3 scripts/present-design.py stop
```

Sync local AIDE copies:

```bash
bash scripts/sync-aide.sh
```

## Repository Layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── aide-integration.md
│   ├── artifact-presentation.md
│   ├── design-defaults.md
│   ├── design-process.md
│   ├── helper-registry.md
│   ├── local-overrides.example.md
│   ├── project-profile.example.md
│   └── review-rubric.md
├── scripts/
│   ├── capture-audit.py
│   ├── detect-frontend-env.sh
│   ├── present-design.py
│   └── sync-aide.sh
└── tests/
    └── test_present_design.py
```

## Validation

Local checks:

```bash
bash -n scripts/*.sh
python3 -m py_compile scripts/*.py
python3 scripts/present-design.py --help >/dev/null
python3 -m unittest discover -s tests -v
bash scripts/detect-frontend-env.sh .
```

The GitHub `validate.yml` workflow also checks the skill frontmatter, script syntax, Python compilation, managed presentation lifecycle, remote fallback behavior, and accidental local path leakage.

## Gitee Mirror

This repository is configured to sync `main` and tags to:

```text
https://gitee.com/synovation/f-design
```

The mirror workflow expects these GitHub repository secrets:

```text
GITEE_USERNAME
GITEE_TOKEN
```

`GITEE_TOKEN` should have repository/project write permission.

## License

MIT. See [LICENSE](LICENSE).
