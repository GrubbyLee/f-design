# AIDE Integration

Use this reference only when the user asks how to install, sync, or invoke `f-design` across AI development environments.

## Local Source of Truth

Primary folder:

```text
~/.codex/skills/f-design
```

Keep this folder as the source of truth. Sync it to other AIDE skill folders when needed.

## Known Local Targets

The following folders exist on this machine:

```text
~/.claude/skills
~/.cursor/skills
~/.qwen/skills
```

Recommended install paths:

```text
~/.claude/skills/f-design
~/.cursor/skills/f-design
~/.qwen/skills/f-design
```

## Invocation Guide

- Codex: "use f-design", `f-design`, `$f-design`, or `@f-design` if the interface supports it.
- Claude Code: `/f-design` when installed as a Claude skill; otherwise say "use f-design".
- Cursor: say "use f-design"; if it does not detect the skill, point it to the local `SKILL.md`.
- Qwen Code: say "use f-design"; if it does not detect the skill, point it to the local `SKILL.md`.
- Unknown AIDE: add the folder to the tool's skill/rule/context directory, or paste the `SKILL.md` path and ask the agent to follow it.

## Sync

Run:

```bash
bash ~/.codex/skills/f-design/scripts/sync-aide.sh
```

The script copies the Codex source folder into Claude, Cursor, and Qwen skill directories.

## Project And Local Preferences

Portable default rules live in the skill folder. Personal preferences should stay outside the public skill source:

```text
.f-design/profile.md
~/.f-design/preferences.md
```

Use these templates when needed:

```text
references/project-profile.example.md
references/local-overrides.example.md
```

Do not hard-code private names, brands, directories, API keys, or personal taste into `SKILL.md` before publishing.

## Compatibility Principle

Do not rely on one product's invocation syntax inside the skill body. The portable contract is:

```text
Read SKILL.md and follow f-design.
```
