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

## 可视化编辑

这个仓库已经加入 CloudCannon 配置文件：`cloudcannon.config.yml`。

把 CloudCannon 连接到 GitHub 仓库 `gpingz/gpingz.github.io` 后，可以在网页后台编辑个人信息、首页文案、项目描述、论文条目，并上传/替换图片。具体步骤见 `CLOUDCANNON.md`。

## 修改文字

最常改的两个位置：

- `data/authors/me.yaml`：改个人简介、经历、教育、技能、奖项。
- `content/_index.md`：改首页 Research 和 Contact 文案。

论文和项目各自是一个文件夹，修改对应文件夹里的 `index.md` 即可。

## 部署建议

当前站点按 GitHub Pages 根域名配置：

- Repository: `gpingz/gpingz.github.io`
- Public URL: `https://gpingz.github.io/`

GitHub Pages 会通过 `.github/workflows/build.yml` 自动构建和发布 HugoBlox 站点。修改内容后提交并推送到 `main` 分支，GitHub Actions 完成后页面会自动更新。

如果以后要换自定义域名，可以在 GitHub Pages 设置里添加域名，并把 `config/_default/hugo.yaml` 里的 `baseURL` 改成对应域名。

## 本地预览

本地需要 Hugo Extended、Node.js 和 pnpm：

```bash
pnpm install
pnpm run dev
```

当前 Codex 环境已临时下载 Hugo Extended，但本地缺少 Go 工具链，且从 Go 官方下载临时 Go 时网络超时，所以本地 Hugo modules 构建可能受限。文件结构和内容已按 HugoBlox Academic CV 模板整理好，可直接交给 GitHub Actions 在线构建。

## 模板来源

Template: HugoBlox Academic CV  
License: MIT
