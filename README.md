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
[![Release](https://img.shields.io/github/v/release/GrubbyLee/f-design)](https://github.com/GrubbyLee/f-design/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> A frontend design orchestration skill for Codex, Claude Code, Cursor, Qwen Code, and other AI development environments.

`f-design` is not another UI style preset. It is a frontend design and production engineering control skill: it helps an AI coding agent understand a repository, choose and present a design direction, lock an executable contract, implement the UI, and verify behavior and quality before delivery.

Current version: **v0.1.0**. See [AIDE compatibility](COMPATIBILITY.md) for separate installed, synchronized, and provider-invoked evidence.

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
- Evaluates existing product/page designs by mode, scores strengths and weaknesses, flags generic AI-design tells, and outputs prioritized, actionable improvement plans with evidence, tradeoffs, acceptance criteria, and verification steps.
- Inventories frameworks, routes, components, tokens, data contracts, test tools, and project risks before substantial implementation.
- Turns approved designs into machine-validated contracts covering flows, states, breakpoints, accessibility, performance budgets, data schemas, visual baselines, and approval evidence.
- Verifies declared interactions at responsive breakpoints with Playwright, console and overflow checks, axe accessibility audits, screenshot comparison, browser metrics, and optional Lighthouse gates.
- Provides state/data guidance and adapters for React/Next/Remix, Vue/Nuxt, SvelteKit, Angular, static HTML, and embedded mobile web.
- Starts real development servers as managed previews with health checks, browser opening, logs, status, and safe cleanup.
- Uses project/local preference files without hard-coding personal taste into the public skill.
- Provides deterministic scripts for project inspection, artifact presentation, contract validation, application previews, interaction QA, visual diffs, screenshot capture, and cross-AIDE syncing.
- Ships behavior regression fixtures, three product-journey acceptance checks, specialized operational-UI review templates, and digest-based cross-AIDE version diagnosis.

## Quick Start

Install for Codex:

```bash
git clone https://github.com/GrubbyLee/f-design.git ~/.codex/skills/f-design
```

Synchronize the same skill across Codex, Claude Code, Cursor, and Qwen Code local skill directories:

```bash
bash ~/.codex/skills/f-design/scripts/sync-aide.sh
python3 ~/.codex/skills/f-design/scripts/f-design-doctor.py --strict
```

The target `f-design` directories are managed mirrors: stale files are removed, while `.git`, `.codex`, generated Python caches, and private `.f-design/profile.md` files are excluded.

The sync script copies the current `f-design` folder to these managed targets. When the source already equals a target, that target is skipped.

```text
~/.codex/skills/f-design
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

3. Evaluate an existing product/page design
   Primary: f-design
   Helpers if available: web-design-guidelines, webapp-testing, design-taste-frontend

4. Add complex animation
   Primary: f-design
   Helpers if available: gsap, animejs

5. Build 3D / WebGL
   Primary: f-design
   Helpers if available: three
```

## Mode 2: Execution

When you provide a real task:

```text
Use f-design to build a creator dashboard for reviewing generated media.
```

You can also ask for a product design review:

```text
Use f-design to evaluate this existing dashboard design and provide a prioritized improvement report.
Input: <URL/screenshot/HTML/repo path>
Output: scorecard, strengths, issues, actionable changes, acceptance criteria.
```

The review workflow separates marketing pages, product workbenches, data dashboards, forms, mobile surfaces, redesign audits, accessibility audits, and competitive comparisons so dense product UI is not judged with landing-page rules.

Specialized templates add deeper evidence and acceptance criteria for data tables, dashboards, complex forms, mobile navigation, and high-risk batch actions. Mobile templates are loaded only when mobile is explicitly in scope or the artifact is mobile-first.

The agent should follow this loop:

1. Inventory the project and read product context.
2. Choose Level 0, 1, or 2 design depth.
3. Define the user's job, information priority, structure, states, data, and success criteria.
4. Select the smallest useful helper capability set.
5. For exploratory work, produce the lowest-cost useful review artifact, present it, and wait for user confirmation.
6. Record the approved design system and executable implementation contract.
7. Build a viewable v0 for substantial work.
8. Implement using the detected framework and repository conventions.
9. Start and present a managed application preview when useful.
10. Run interaction, state, accessibility, responsive, visual, console, and performance QA.
11. Run the repository's build, lint, typecheck, and tests.
12. Enforce no-ship gates before claiming completion.

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

Generate structured project intelligence:

```bash
python3 scripts/inspect-project.py . --format markdown
```

Create and validate an executable design contract:

```bash
python3 scripts/design-contract.py init --out .codex/f-design/design-contract.json
python3 scripts/design-contract.py validate .codex/f-design/design-contract.json --project-root . --require-approved
```

Start, inspect, and stop a real application preview:

```bash
python3 scripts/run-preview.py start --command "npm run dev" --url http://127.0.0.1:3000
python3 scripts/run-preview.py status
python3 scripts/run-preview.py stop
```

Run contract-driven browser QA:

```bash
python3 scripts/verify-ui.py http://127.0.0.1:3000 \
  --contract .codex/f-design/design-contract.json --project-root .
```

Compare a screenshot against a visual baseline:

```bash
python3 scripts/visual-diff.py baseline.png current.png --diff-out diff.png
```

Run lightweight frontend environment detection:

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

Check versions and public-file digests across all supported AIDEs:

```bash
python3 scripts/f-design-doctor.py --strict
```

Run an explicit provider-backed invocation smoke test (may consume model quota):

```bash
python3 scripts/smoke-aides.py --aide codex --yes-consume-provider-quota
```

Run the deterministic design-approval, review-isolation, and cross-AIDE product journeys:

```bash
python3 scripts/verify-product-journeys.py
```

Evaluate a captured agent review against a scope contract:

```bash
python3 scripts/evaluate-review-output.py \
  tests/fixtures/review-behavior/image-review-isolated.json \
  response.md
```

## Repository Layout

```text
.
├── SKILL.md
├── VERSION
├── f-design.json
├── CHANGELOG.md
├── COMPATIBILITY.md
├── RELEASE_NOTES.md
├── UPGRADING.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── aide-integration.md
│   ├── anti-ai-design-tells.md
│   ├── artifact-presentation.md
│   ├── design-contract.schema.json
│   ├── design-defaults.md
│   ├── design-process.md
│   ├── framework-adapters.md
│   ├── helper-registry.md
│   ├── implementation-contract.md
│   ├── local-overrides.example.md
│   ├── project-intelligence.md
│   ├── project-profile.example.md
│   ├── product-design-review.md
│   ├── end-to-end-journeys.md
│   ├── review-templates/
│   ├── quality-gates.md
│   ├── state-and-data.md
│   └── review-rubric.md
├── scripts/
│   ├── capture-audit.py
│   ├── design-contract.py
│   ├── check-secrets.py
│   ├── evaluate-review-output.py
│   ├── f-design-doctor.py
│   ├── detect-frontend-env.sh
│   ├── present-design.py
│   ├── inspect-project.py
│   ├── run-preview.py
│   ├── smoke-aides.py
│   ├── sync-aide.sh
│   ├── verify-ui.py
│   ├── verify-product-journeys.py
│   └── visual-diff.py
└── tests/
    ├── fixtures/quality/
    ├── fixtures/review-behavior/
    ├── test_behavior_evaluations.py
    ├── test_documentation_contract.py
    ├── test_present_design.py
    ├── test_quality_pipeline.py
    ├── test_release_tooling.py
    └── test_support_scripts.py
```

## Validation

Local checks:

```bash
bash -n scripts/*.sh
python3 -m py_compile scripts/*.py
python3 scripts/present-design.py --help >/dev/null
python3 scripts/capture-audit.py --help >/dev/null
python3 scripts/design-contract.py validate tests/fixtures/quality/design-contract.json --project-root . --require-approved
python3 -m unittest discover -s tests -v
python3 scripts/verify-product-journeys.py
python3 scripts/check-secrets.py .
bash scripts/detect-frontend-env.sh .
```

The GitHub `validate.yml` workflow also runs a strict browser-quality job against the fixture contract with Playwright Chromium, axe-core, responsive state/keyboard flows, screenshots, and Lighthouse. Verification reports and screenshots are uploaded as workflow artifacts.

## Versioning And Releases

The current release is declared in `VERSION` and `f-design.json`. See `CHANGELOG.md` for changes, `RELEASE_NOTES.md` for the current release summary, and `UPGRADING.md` for safe upgrade instructions. Provider-side AIDE invocation remains an explicit, separately reported check because it can consume external model quota.

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
