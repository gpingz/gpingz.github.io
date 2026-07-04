# Guangping Zeng - HugoBlox Academic CV 个人主页

这个版本基于 HugoBlox 的 Academic CV 模板定制，内容已替换为 Guangping Zeng 的 CV 信息，包括个人简介、研究方向、经历、教育、技能、荣誉、项目和论文。

## 主要文件

- `content/_index.md`：首页区块配置。
- `data/authors/me.yaml`：个人简介、经历、教育、技能、奖项和联系方式。
- `content/publications/`：论文和会议摘要条目。
- `content/projects/`：研究项目条目。
- `static/uploads/resume.pdf`：主页 Download CV 按钮链接的 CV。
- `assets/media/authors/me.png`：头像。

## 替换照片

头像：

- 用你的真实头像覆盖 `assets/media/authors/me.png`。

项目图片：

- 覆盖 `content/projects/makran-carbon-cycling/featured.jpg`
- 覆盖 `content/projects/pakistan-cenozoic-volcanism/featured.jpg`
- 覆盖 `content/projects/south-poyang-basin/featured.jpg`

## 修改文字

最常改的两个位置：

- `data/authors/me.yaml`：改个人简介、经历、教育、技能、奖项。
- `content/_index.md`：改首页 Research 和 Contact 文案。

论文和项目各自是一个文件夹，修改对应文件夹里的 `index.md` 即可。

## 部署建议

推荐 Netlify，因为模板自带 `netlify.toml`，已经配置了 Hugo 0.163.3、Node 和构建命令。

Netlify 步骤：

1. 把整个 `personal-homepage-hugoblox` 文件夹上传到 GitHub 仓库。
2. 在 Netlify 新建站点并连接该仓库。
3. Netlify 会读取 `netlify.toml` 自动构建，发布目录为 `public`。

GitHub Pages 也可以部署，但需要使用 GitHub Actions 构建 Hugo 站点。模板已经包含 `.github/workflows/`，可以按你的仓库设置再调整。

## 本地预览

本地需要 Hugo Extended、Node.js 和 pnpm：

```bash
pnpm install
pnpm run dev
```

当前 Codex 环境已临时下载 Hugo Extended，但本地缺少 Go 工具链，且从 Go 官方下载临时 Go 时网络超时，所以我没有完成本地 Hugo modules 构建。文件结构和内容已按 HugoBlox Academic CV 模板整理好，可直接交给 Netlify 或 GitHub Actions 在线构建。

## 模板来源

Template: HugoBlox Academic CV  
License: MIT
