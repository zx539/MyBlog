# 张迅个人博客

这是一个 Hugo 个人博客站点，适合部署到 GitHub Pages。结构按后续维护拆分：

- `data/profile.yaml`：首页个人信息、技能、项目经历。
- `content/posts/`：博客文章，新增 Markdown 文件即可。
- `content/about.md`、`content/resume.md`：固定页面内容。
- `layouts/partials/`：页面模块组件。
- `assets/css/main.css`：卡通动漫风格样式。
- `static/images/`、`static/files/`：图片和简历 PDF。

## 本地预览

```bash
hugo server -D
```

## 新增文章

```bash
hugo new posts/my-new-post.md
```

## GitHub Pages 部署

1. 把 `hugo.toml` 里的 `baseURL` 改成你的 GitHub Pages 地址。
2. 推送到 GitHub 仓库。
3. 等待 Actions 生成 `gh-pages` 分支。
4. 在仓库 `Settings -> Pages` 里选择 `Deploy from a branch`。
5. 分支选择 `gh-pages`，目录选择 `/ (root)`。
