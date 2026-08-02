# Frontend Review Rubric

Use this when auditing a frontend artifact before delivery or when the user asks whether the UI is good.

## Score

Score each category from 0 to 10. Anything below 8 needs revision unless the user asked for a rough prototype.

- Direction fit: the UI matches the stated product, audience, and reference anchors.
- Visual hierarchy: the eye path is obvious; primary actions and key data dominate.
- Craft: alignment, spacing, color count, typography, radius, shadow, and icon style are consistent.
- Usability: common states exist; workflows are efficient; controls are recognizable.
- Responsiveness: desktop, tablet, and mobile are usable without overlap or text clipping.
- Originality: avoids generic AI gradients, repeated equal cards, vague hero copy, and decorative filler.

## Critical Issues

Fix these before delivery:

- Text overlaps, clips, or escapes its container.
- Mobile layout requires horizontal scrolling unless intentionally designed.
- Primary action is unclear.
- Contrast prevents comfortable reading.
- Dynamic content changes element sizes in a jarring way.
- Decorative layout makes an operational tool harder to use.
- Placeholder assets are presented as finished assets.
- The style drifts across sections.

## Fast Visual Audit

Run this mental checklist against screenshots:

1. Squint test: can you identify the primary region and action in two seconds?
2. Grid test: do major edges align consistently?
3. Density test: does the amount of information match the usage context?
4. Palette test: is there one dominant neutral system and one accent?
5. Component test: do buttons, inputs, cards, tabs, and menus share one visual language?
6. Breakpoint test: does mobile look intentionally designed, not merely squeezed?
