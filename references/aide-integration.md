# AIDE Integration

Use this reference only when the user asks how to install, sync, or invoke `f-design` across AI development environments.

## Local Source of Truth

Primary folder:

```text
~/.codex/skills/f-design
```

Use the current repository as the source of truth. A conventional Codex installation uses the folder above; the sync script safely skips it when source and target are identical.

## Known Local Targets

Supported local skill roots:

```text
~/.codex/skills
~/.claude/skills
~/.cursor/skills
~/.qwen/skills
```

Recommended install paths:

```text
~/.codex/skills/f-design
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

The script copies the source folder into Codex, Claude, Cursor, and Qwen skill directories. It skips any target that resolves to the source itself.

Each target is a managed mirror. Files that no longer exist in the source are removed. Repository metadata, temporary review artifacts, generated Python caches, and `.f-design/profile.md` are excluded.

For an isolated verification or managed environment, redirect only the target root:

```bash
F_DESIGN_TARGET_HOME=/path/to/sandbox \
  bash ~/.codex/skills/f-design/scripts/sync-aide.sh
```

The source can be overridden independently with `F_DESIGN_SRC`.

## Compatibility Verification

Use three levels of evidence and report them separately:

1. **Installed:** the AIDE CLI and its `f-design/SKILL.md` path exist.
2. **Synchronized:** the installed copy matches the source after documented exclusions.
3. **Invoked:** the AIDE is asked to use `f-design` and demonstrates navigation or execution behavior in a real session.

Do not report version checks or file synchronization as successful invocation. Real invocation may contact an external model provider, so run it only when that external request is authorized.

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
