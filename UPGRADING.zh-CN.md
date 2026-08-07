# 升级 f-design

Git 安装方式：

```bash
git pull --ff-only
```

然后同步并检查所有 AIDE 镜像：

```bash
bash scripts/sync-aide.sh
python3 scripts/f-design-doctor.py --strict
```

本地偏好仍保存在 `.f-design/profile.md` 和 `~/.f-design/preferences.md`，不会被公开源覆盖。升级后如果 AIDE 缓存了 skill 发现结果，请重启或重新加载 AIDE。
