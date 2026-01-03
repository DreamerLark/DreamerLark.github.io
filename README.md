# 刘建的 Markdown 主页

这个仓库改为纯 Markdown 方式维护，便于直接在 GitHub 或 GitHub Pages 上浏览学习记录。

## 快速入口
- 主页导航：[`index.md`](./index.md)
- Codex 学习记录：[`codex.md`](./codex.md)
- GitHub 主页：https://github.com/DreamerLark

## 在 GitHub Pages 上查看
1. 仓库 Settings → Pages，选择 Source 为 **GitHub Actions**（推荐）。如果使用分支方式，请确保选择 `master`（当前 Pages 允许部署的分支）和 `/` 目录。
2. 保存后等待几分钟，页面会发布到 `https://<用户名>.github.io/<仓库名>/`（若为用户主页仓库，则为 `https://<用户名>.github.io/`）。
3. 本仓库已放置 `.nojekyll`，确保静态 Markdown 原样渲染。
4. 已添加自动同步：`main` 分支 push 时，会运行工作流自动将 `main` 强制推送覆盖到 `master`，确保 Pages 始终使用最新内容（见 `.github/workflows/sync-main-to-master.yml`）。若 `master` 有保护规则，请在受控场景下暂时放宽，或手动同步。

> 已提供 `.github/workflows/pages.yml`，会在 `main` 分支 push 时自动部署到 GitHub Pages，避免旧的 `master` 分支内容被展示。

## 简述
- “老程序员的日常， 坚持就是胜利”。
- 专注记录大模型辅助编程的学习笔记与最佳实践。
