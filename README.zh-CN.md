# f-design

[English](README.md) | 简体中文

[![Validate](https://github.com/GrubbyLee/f-design/actions/workflows/validate.yml/badge.svg)](https://github.com/GrubbyLee/f-design/actions/workflows/validate.yml)
[![Sync to Gitee](https://github.com/GrubbyLee/f-design/actions/workflows/sync-to-gitee.yml/badge.svg)](https://github.com/GrubbyLee/f-design/actions/workflows/sync-to-gitee.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> 面向 Codex、Claude Code、Cursor、Qwen Code 及其他 AI 开发环境的前端设计总控 skill。

`f-design` 不是又一个 UI 风格预设，而是一个前端总控 skill：它帮助 AI 编程助手读取产品上下文、判断设计方向、选择辅助 skill、构建 v0、完成实现，并在交付前进行截图验收。

它的目标是减少模板化、AI 味明显的前端界面，让前端设计和开发形成稳定闭环。

## 它解决什么

- 作为前端入口 skill 和能力导航器。
- 支持两种模式：
  - **导航模式**：没有具体需求时，不写代码，主动列出当前环境可做的前端任务和辅助 skill。
  - **执行模式**：有具体需求时，按设计判断、设计系统、v0、实现、截图 QA 的流程推进。
- 能分流后台、管理端、工具界面、落地页、重设计、截图还原、移动端、动效、3D、UI 审查等任务。
- 支持项目级和本机级偏好文件，不把个人偏好写死进开源 skill。
- 内置前端环境探测、截图 QA、跨 AIDE 本地同步脚本。

## 快速开始

安装到 Codex：

```bash
git clone https://github.com/GrubbyLee/f-design.git ~/.codex/skills/f-design
```

可选：同步到 Claude Code、Cursor、Qwen Code 的本地 skill 目录：

```bash
bash ~/.codex/skills/f-design/scripts/sync-aide.sh
```

同步目标：

```text
~/.claude/skills/f-design
~/.cursor/skills/f-design
~/.qwen/skills/f-design
```

## 调用方式

不同 AIDE 的 skill 调用语法不完全一致。最通用的方式是：要求 agent 使用 `f-design`。

| 环境 | 推荐调用 |
|---|---|
| Codex | `use f-design`、`f-design`、`$f-design`，或界面支持时用 `@f-design` |
| Claude Code | 安装为 Claude skill 后用 `/f-design`，或直接说 `use f-design` |
| Cursor | 说 `use f-design`，或让 agent 读取 `SKILL.md` |
| Qwen Code | 说 `use f-design`，或让 agent 读取 `SKILL.md` |
| 其他 AIDE | 让 agent 读取 `SKILL.md` 并遵循 `f-design` |

## 模式一：导航

当你只输入：

```text
f-design
```

agent 不应该直接写代码，而应该列出可用前端能力，例如：

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

## 模式二：执行

当你给出具体任务：

```text
使用 f-design 帮我做一个用于审核生成媒体的创作者后台。
```

agent 应该按这个流程推进：

1. 读取产品上下文。
2. 写出设计判断和设计系统，再开始编码。
3. 选择最少但必要的辅助能力。
4. 对较大任务先做可浏览 v0。
5. 遵循现有技术栈和代码风格完成实现。
6. 对桌面、平板、手机进行截图 QA。
7. 通过 No-Ship Gates 后再声称完成。

## 偏好文件

`f-design` 把开源默认规则与个人/项目偏好分离。

读取顺序：

```text
1. 当前项目的 .f-design/profile.md
2. 本机的 ~/.f-design/preferences.md
3. skill 自带的 references/design-defaults.md
```

模板：

```text
references/project-profile.example.md
references/local-overrides.example.md
```

不要把私人姓名、路径、API Key 或个人偏好提交到公开 skill。

## 脚本

探测前端环境：

```bash
bash scripts/detect-frontend-env.sh .
```

截取桌面、平板、手机截图：

```bash
python3 scripts/capture-audit.py http://localhost:3000 --out .codex/frontend-audit
```

同步本地 AIDE 副本：

```bash
bash scripts/sync-aide.sh
```

## 仓库结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── aide-integration.md
│   ├── design-defaults.md
│   ├── helper-registry.md
│   ├── local-overrides.example.md
│   ├── project-profile.example.md
│   └── review-rubric.md
└── scripts/
    ├── capture-audit.py
    ├── detect-frontend-env.sh
    └── sync-aide.sh
```

## 校验

本地校验：

```bash
bash -n scripts/*.sh
python3 -m py_compile scripts/*.py
bash scripts/detect-frontend-env.sh .
```

GitHub `validate.yml` workflow 会检查 skill frontmatter、脚本语法、Python 编译，以及是否意外包含本机路径。

## Gitee 镜像

本仓库配置了将 `main` 和 tags 同步到：

```text
https://gitee.com/synovation/f-design
```

同步 workflow 需要 GitHub 仓库 Secrets：

```text
GITEE_USERNAME
GITEE_TOKEN
```

`GITEE_TOKEN` 需要具备仓库/项目写入权限。

## License

MIT。见 [LICENSE](LICENSE)。
