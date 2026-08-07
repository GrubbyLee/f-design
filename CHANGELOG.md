# Changelog

All notable changes to `f-design` are documented here. The project follows Semantic Versioning from `v0.1.0` onward.

## [0.1.0] - 2026-08-07

### Added

- Level 0/1/2 design-depth routing with explicit user confirmation for exploratory work.
- Automatic presentation of standalone HTML and managed review servers.
- Machine-validated implementation contracts with approval evidence, flows, states, accessibility, performance, data, and visual gates.
- Project intelligence, managed preview, screenshot capture, visual diff, and strict browser QA scripts.
- Existing product/page design evaluation with evidence, scorecards, priorities, tradeoffs, acceptance criteria, and before/after comparison.
- Scope Gate rules that prevent unrequested mobile, accessibility, implementation, redesign, or publishing work and forbid inherited side goals.
- Behavior-level review fixtures for the historical mobile/WeChat context-leak regression.
- Specialized review templates for data tables, dashboards, complex forms, mobile navigation, and high-risk batch operations.
- Cross-AIDE version manifest, digest-based synchronization, and `f-design-doctor.py` for Codex, Claude Code, Cursor, and Qwen Code.
- Three deterministic end-to-end product journey checks.
- Depth Stack visual identity and bilingual documentation.

### Changed

- CI secret scanning now uses boundary-aware token detection to avoid false positives such as ordinary `task-based` prose.
- Cross-AIDE sync excludes repository workflows, promotional artifacts, caches, private profiles, and generated review files.

### Known Limitations

- Provider-side invocation tests are not automatic because they can consume external model quota and require explicit authorization.
- Browser QA requires Playwright/Chromium; accessibility and Lighthouse gates require their declared local tools.
- Design quality still depends on the host model following the skill and on sufficient product context/evidence.
