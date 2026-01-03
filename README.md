# 刘建的 Markdown 主页

这个仓库改为纯 Markdown 方式维护，便于直接在 GitHub 或 GitHub Pages 上浏览学习记录。工作流会自动将 Markdown 转成 HTML，避免手工维护静态页面。

## 快速入口
- 主页导航：[`index.md`](./index.md)
- Codex 学习记录：[`codex.md`](./codex.md)
- GitHub 主页：https://github.com/DreamerLark
> GitHub Pages 需要静态主页文件，工作流会从 Markdown 动态生成 `index.html`、`codex.html` 等静态页面，可直接访问 `https://dreamerlark.github.io/`。

## 在 GitHub Pages 上查看
1. 仓库 Settings → Pages，选择 Source 为 **GitHub Actions**（推荐）。如果使用分支方式，请确保选择 `master`（当前 Pages 允许部署的分支）和 `/` 目录。
2. 保存后等待几分钟，页面会发布到 `https://<用户名>.github.io/<仓库名>/`（若为用户主页仓库，则为 `https://<用户名>.github.io/`）。
3. 本仓库已放置 `.nojekyll`，确保静态 Markdown 原样渲染。
4. 已添加自动同步：`main` 分支 push 时，会运行工作流自动将 `main` 强制推送覆盖到 `master`，确保 Pages 始终使用最新内容（见 `.github/workflows/sync-main-to-master.yml`）。若 `master` 有保护规则，请在受控场景下暂时放宽，或手动同步。
5. 若希望同步后自动触发 Pages 部署，请在仓库 Secrets 中配置 `SYNC_PAT`（具备 `repo` 权限的个人访问令牌）。使用 PAT 推送到 `master` 可触发下游的 Pages 工作流；若未配置，将使用 `GITHUB_TOKEN`，此时 GitHub 不会触发其他工作流，需要手动运行部署。

## 构建说明
- Pages 工作流会在部署前自动执行 `scripts/build_html.py`，使用 `markdown` 包把顶层的 Markdown（`index.md`、`codex.md`、`README.md`）转换为 HTML。你可以本地运行 `python scripts/build_html.py` 检查生成结果。
- 如果需要定制样式或导航，可直接修改 `scripts/build_html.py` 中的模板和导航链接。

> 已提供 `.github/workflows/pages.yml`，会在 `main` 分支 push 时自动部署到 GitHub Pages，避免旧的 `master` 分支内容被展示。

## 简述
- “老程序员的日常， 坚持就是胜利”。
- 专注记录大模型辅助编程的学习笔记与最佳实践。
