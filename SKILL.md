---
name: f-design
description: Frontend design orchestrator and skill navigator. Use when the user invokes f-design, @f-design, /f-design, asks for frontend design/development/redesign, web app UI, dashboard, tool interface, landing page, responsive React/HTML/CSS work, screenshot QA, or says they are dissatisfied with generic AI-looking UI. If invoked without a concrete task, enter navigation mode and recommend the best available frontend-related skills/tools for the user's environment instead of coding.
---

# F Design

Use this as the frontend entry skill. It is not a single visual style; it is the controller for frontend product thinking, implementation, auxiliary skill selection, and screenshot QA.

## Context Files

Before substantial work, look for preference files in this order:

1. `.f-design/profile.md` in the current project.
2. `~/.f-design/preferences.md` on the local machine.
3. `references/design-defaults.md` bundled with this skill.

Read only the files that exist and are relevant. Project and local files override bundled defaults. Keep personal preferences out of the skill folder so the skill remains open-source friendly.

## Invocation Modes

### Mode 1: Navigation

Use this mode when the user only says `f-design`, `@f-design`, `/f-design`, "use f-design", or otherwise gives no concrete frontend task.

Reply with a concise menu of what the environment can do. Do not code. Do not invent unavailable skills.

1. Inspect the available skill/tool list if the host exposes one.
2. Read `references/helper-registry.md`.
3. Group relevant capabilities by task, not by skill name.
4. Recommend the best primary path and optional helpers.
5. Give 2-3 example prompts the user can run next.

Navigation output should look like:

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

If a helper is not visible in the current AIDE, say "not detected here" and continue with the best fallback.

### Mode 2: Execution

Use this mode when the user gives a real frontend task.

Do not start coding immediately unless the task is a tiny isolated UI fix. First produce a design read and concrete design system. For substantial work, build a viewable v0 before completing the full interface.

## Task Routing

Route the user's wording before selecting tools:

- "build a dashboard/admin/tool/editor" -> product screen workflow; make the usable working surface first.
- "make this prettier/redesign/looks AI-generated" -> taste correction workflow; preserve existing function and fix visual hierarchy.
- "match this screenshot/image" -> screenshot-to-code workflow; use screenshot helpers if available.
- "landing page/site/homepage" -> brand or landing workflow; verify product/brand facts when current or specific.
- "animation/motion/transition" -> motion workflow; pick CSS/WAAPI/GSAP/Anime based on complexity and existing dependencies.
- "mobile/miniprogram/responsive" -> mobile-first workflow; audit narrow widths before desktop polish.
- "review/audit/check UX" -> review workflow; read `references/review-rubric.md`.

## AIDE Compatibility

Treat `f-design` as tool-neutral.

- Codex: invoke with "use f-design", `f-design`, `$f-design`, or `@f-design` if the UI supports mentions.
- Claude Code: invoke with `/f-design` when the skill is installed in the Claude skill directory; natural language "use f-design" is the fallback.
- Cursor: invoke by asking the agent to use `f-design` or by pointing it at this `SKILL.md`; if Cursor skill discovery is configured, install this folder under Cursor's skill directory.
- Qwen Code: invoke by asking the agent to use `f-design`; if Qwen skill discovery is configured, install this folder under Qwen's skill directory.
- Other AIDE: use the same folder as a portable skill; if the tool has no skill protocol, tell the agent to read `SKILL.md` and follow `f-design`.

For local setup details, read `references/aide-integration.md` only when the user asks about installing, syncing, or using this skill in another AIDE.

## Workflow

### 1. Read the product context

State one line:

```text
Reading this as: <page/app type> for <audience>, with a <vibe> language, leaning toward <design system or reference family>.
```

Infer from the user request, repo, screenshots, existing CSS, `package.json`, named references, and business context. Ask one concise question only when the design direction genuinely splits.

When working inside a codebase, run `scripts/detect-frontend-env.sh` when helpful:

```bash
bash scripts/detect-frontend-env.sh .
```

### 2. Declare the design system

Before code, write:

- Product role: operational tool, dashboard, editor, landing page, content site, prototype, etc.
- Audience and use frequency.
- Reference anchors: real apps, brands, design systems, or local existing UI.
- Color system: neutral base, one accent, semantic colors.
- Typography: display/body/code fonts or existing project font.
- Spacing: base unit and container width.
- Radius: one radius strategy.
- Elevation: border, shadow, or flat hierarchy.
- Motion: duration, easing, interaction triggers, reduced-motion behavior.
- Anti-defaults: what must be avoided for this project.

For operational tools, admin panels, creator dashboards, and editors, prefer dense but calm working screens over marketing heroes, decorative cards, and large empty sections.

### 3. Select helper capabilities

Before implementation, decide if auxiliary skills/tools are useful. Prefer the host's discovered names. Do not require the user to remember them. Read `references/helper-registry.md` when the selection is not obvious.

- General polished web artifact: use `web-design-engineer` if available.
- Landing page, portfolio, redesign taste correction: use `design-taste-frontend` if available.
- UI audit, accessibility, best-practice review: use `web-design-guidelines` if available.
- Browser screenshot/testing: use `webapp-testing` or local Playwright.
- Complex motion: use `gsap`, `animejs`, `css-animations`, or `waapi` based on the project stack.
- 3D/WebGL: use `three` if available.
- Screenshot-to-code: use `image-to-code` or `yueban-image-to-code` if available.
- Generated UI assets: use image generation skills only when the user asks for visual assets or the design requires them.

If no helper is available, continue with native framework/CSS and state the fallback briefly.

### 4. Build a v0 first

For new screens or major redesigns, implement a v0 with:

- Real page layout and navigation.
- Representative content, not lorem ipsum.
- Main visual hierarchy and responsive structure.
- Key empty/loading/error states if they affect layout.
- Placeholder assets only when real assets are unavailable.

Stop after v0 only if the user asked to confirm direction. Otherwise continue when the user granted autonomy.

### 5. Full implementation

Follow the existing stack and code style first. Check `package.json` before importing libraries. Do not add a new UI library unless the project lacks one and the dependency is justified.

Implementation rules:

- Use existing components, tokens, helpers, and routing conventions.
- Avoid nested cards and section-as-card page structure.
- Use icons from the existing icon family; do not hand-roll SVG icons.
- Implement hover, focus, disabled, loading, empty, error, and long-text states where relevant.
- Keep text inside buttons and fixed UI elements stable across breakpoints.
- Use CSS Grid for page structure when flex width math would be fragile.
- Do not use viewport-scaled font sizes.
- Avoid default AI-purple/blue gradients unless brand-justified.
- Do not make a landing page when the user asked for a product, app, dashboard, tool, or editor; make the usable screen first.

### 6. Screenshot QA

After implementation, run the local app and capture at least:

- Desktop: `1440x900`
- Tablet: `1024x768`
- Mobile: `390x844`

Use `scripts/capture-audit.py` when helpful:

```bash
python3 scripts/capture-audit.py http://localhost:3000 --out .codex/frontend-audit
```

Inspect screenshots before final. Check text overflow, overlapping UI, broken spacing, unreadable contrast, mobile navigation, blank canvases, and whether the page still matches the design read.

If reviewing a built artifact, read `references/review-rubric.md`.

### 7. No-Ship Gates

Do not claim completion when any required gate fails:

- The app/page cannot be opened locally.
- No screenshot or visual inspection was performed for a substantial visual change.
- Mobile layout has obvious overflow, overlap, or unusable navigation.
- Text is clipped inside buttons, cards, tabs, or fixed-size controls.
- The result ignores the declared design read.
- Typecheck/build/lint fails and the failure is related to the change.
- The page looks like a generic AI SaaS template after logo/text substitution.

For substantial UI work, self-score before final:

```text
Hierarchy: 0-10
Consistency: 0-10
Mobile: 0-10
Usability: 0-10
Originality: 0-10
```

If any score is below 8, revise before delivery or clearly report why it cannot be fixed in this pass.

### 8. Final response

Report:

- What changed.
- Where to open it.
- Screenshot/device checks performed.
- Tests or type checks run.
- Remaining risks if anything could not be verified.

Keep the response concise.

## Quality Bar

The result should look like it belongs to this exact product and audience. If it could be pasted into any AI SaaS template with only the logo changed, revise before delivering.
