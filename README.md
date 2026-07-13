# 风间惟花个人博客

这是一个 Hugo 个人博客站点，适合部署到 GitHub Pages。结构按后续维护拆分：

- `data/profile.yaml`：首页个人信息、技能、项目经历。
- `content/posts/`：博客文章，新增 Markdown 文件即可。
- `content/about.md`：个人介绍页面。
- `layouts/partials/`：页面模块组件。
- `assets/css/main.css`：卡通动漫风格样式。
- `static/images/`：头像、背景图等图片资源。
- `data/daily.yaml`、`static/images/daily/`：每日一景配置与独立图片。
- `docs/CONTENT_API.md`：所有内容模块的字段和更新方法。

## 本地预览

```bash
hugo server -D
```

## 新增文章

```bash
hugo new posts/my-new-post.md
```

## GitHub Pages 部署

1. 确认 `hugo.toml` 中的 `baseURL` 为 `https://zx539.github.io/MyBlog/`。
2. 将修改提交并推送到 GitHub 仓库的 `main` 分支。
3. 在仓库的 `Actions` 页面等待 `Deploy Hugo site to Pages` 工作流完成。
4. 首次部署时，进入 `Settings -> Pages`，将 Source 设为 `Deploy from a branch`。
5. Branch 选择 `gh-pages`，目录选择 `/ (root)`，保存后等待几分钟。
6. 访问 `https://zx539.github.io/MyBlog/`。
