# 风间惟花个人博客

这是一个 Hugo 个人博客站点，适合部署到 GitHub Pages。结构按后续维护拆分：

- `data/profile.yaml`：首页个人信息、技能、项目经历。
- `content/posts/`：博客文章，新增 Markdown 文件即可。
- `content/about.md`：个人介绍页面。
- `layouts/partials/`：页面模块组件。
- `assets/css/main.css`：卡通动漫风格样式。
- `static/images/`：头像、favicon、背景图等图片资源。
- `data/daily.yaml`、`static/images/daily/`：每日一景配置与独立图片。
- `data/friends.yaml`、`static/images/friends/`：友情链接信息与本地头像。
- `docs/CONTENT_API.md`：所有内容模块的字段和更新方法。

## 本地预览

```bash
hugo server -D
```

生产构建与路径检查：

```bash
hugo --gc --minify --cleanDestinationDir --panicOnWarning
```

## 新增文章

```bash
hugo new posts/my-new-post.md
```

文章由 Hugo Goldmark 渲染，支持标题锚点、列表、任务列表、定义列表、表格、引用、代码高亮、图片说明和脚注。具体格式见 `docs/CONTENT_API.md`。

## 常用内容更新

- 修改昵称、签名、头像和项目：编辑 `data/profile.yaml`。
- 修改浏览器标签图标：替换 `static/images/favicon.png` 和 `static/images/apple-touch-icon.png`。
- 添加友情链接：将头像放进 `static/images/friends/`，再向 `data/friends.yaml` 追加对象。
- 替换每日一景：添加图片到 `static/images/daily/`，再修改 `data/daily.yaml`。
- 替换背景视频：覆盖 `static/media/background.mp4`，保留 MP4/H.264 格式。

## GitHub Pages 部署

1. 将 GitHub 仓库命名为 `zx539.github.io`，这是用户主页使用根域名的必要条件。
2. 确认 `hugo.toml` 和 `.github/workflows/hugo.yml` 中的地址均为 `https://zx539.github.io/`，再将修改推送到发布分支。
3. 在仓库的 `Actions` 页面等待 `Deploy Hugo site to Pages` 工作流完成。
4. 首次部署时，进入 `Settings -> Pages`，将 Source 设为 `Deploy from a branch`。
5. Branch 选择 `gh-pages`，目录选择 `/ (root)`，保存后等待几分钟。
6. 访问 `https://zx539.github.io/`。
