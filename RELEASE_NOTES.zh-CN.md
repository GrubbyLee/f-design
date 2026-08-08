# design-guide v0.1.2

`v0.1.2` 是一个命名一致性补丁版本，将显示名称、配置目录以及全部文档与 `design-guide` 品牌统一对齐。

## 主要变更

- **显示名称**：SKILL.md 标题由 "F Design" 改为 "Design Guide"（修复 ClawHub 技能卡片名称）。
- **配置目录**：所有引用统一为 `.design-guide/` 作为项目偏好路径。
- **清单文件**：`design-guide.json` 版本升至 `0.1.2`。

## 升级方式

```bash
git pull --ff-only
bash scripts/sync-aide.sh
python3 scripts/design-guide-doctor.py --strict
```


# design-guide v0.1.1

`v0.1.1` 是一次修复发布，保留 `v0.1.0` 的完整设计到实现工作流，并加强发布完整性、密钥扫描、版本一致性和跨 AIDE 同步安全。

升级命令：

```bash
git pull --ff-only
bash scripts/sync-aide.sh
python3 scripts/design-guide-doctor.py --strict
```
