# 博客内容接口文档

本站是 Hugo 静态网站，没有运行时 HTTP 后端接口。这里的“接口”指数据文件、Markdown 内容和静态资源之间的稳定约定。修改数据后运行 Hugo，模板会读取这些接口并生成页面。

## 1. 目录总览

| 功能 | 数据或内容 | 图片目录 | 渲染模板 |
| --- | --- | --- | --- |
| 个人信息 | `data/profile.yaml` | `static/images/` | `home-sidebar.html`、`hero.html`、`home-rail.html`、`footer.html` |
| 每日一景 | `data/daily.yaml` | `static/images/daily/` | `home-rail.html` |
| 博客文章 | `content/posts/*.md` | `static/images/posts/` | `posts.html`、`list.html`、`single.html` |
| 项目经历 | `data/profile.yaml` 的 `projects` | 可选 `static/images/projects/` | `projects.html` |
| 技能标签 | `data/profile.yaml` 的 `skills` | 无 | `home-sidebar.html`、`skills.html` |
| 友情链接 | `data/friends.yaml` | 无 | `home-rail.html`、`friends.html` |
| 关于页面 | `content/about.md` | 可选 `static/images/about/` | `single.html` |
| 首页导航顺序 | `layouts/partials/home-sidebar.html` | 无 | `home-sidebar.html` |

所有静态资源路径都相对于 `static/`。例如配置中的 `images/profile.jpg` 对应磁盘文件 `static/images/profile.jpg`。

## 2. 个人信息接口

文件：`data/profile.yaml`

### 基础字段

```yaml
name: 风间惟花
role: AI Agent 开发者 / 全栈开发 / 架构设计
tagline: 长叹息以掩涕兮，哀民生之多艰。
location: 克拉玛依市 / 东北大学秦皇岛分校
email: 202412724@stu.neuq.edu.cn
qq: "2198762717"
avatar: images/profile.jpg
hero_art: images/fox-girl-background-v2.webp
template: images/template.jpg
```

| 字段 | 必填 | 用途 | 修改方法 |
| --- | --- | --- | --- |
| `name` | 是 | 昵称、头像旁署名、页面品牌 | 直接修改字符串 |
| `role` | 是 | 职业说明 | 使用 `/` 分隔多个身份 |
| `tagline` | 是 | 首页签名和 About Me 签名 | 直接修改字符串 |
| `location` | 是 | 右栏所在地 | 直接修改字符串 |
| `email` | 是 | 左栏、右栏和底栏邮箱链接 | 填写完整邮箱，不要添加 `mailto:` |
| `qq` | 是 | 左栏、右栏和底栏 QQ | 必须加引号，防止被 YAML 当数字处理 |
| `avatar` | 是 | 头像 | 图片放进 `static/images/` 后填写相对路径 |
| `hero_art` | 是 | 首页狐狸娘背景 | 建议使用 16:9、宽度至少 1600px 的图片 |
| `template` | 否 | 设计参考图路径 | 不直接显示在页面中 |

### 添加技能

在 `skills` 数组末尾新增一行：

```yaml
skills:
  - Python
  - Rust
```

左栏只显示前 9 项，完整技能组件会显示所有项目。调整顺序时直接移动数组行。

### 添加首页关注方向

在 `highlights` 数组中添加内容：

```yaml
highlights:
  - AI Agent 开发
  - 新的研究方向
```

首页封面底部显示前 4 项。

### 添加项目经历

在 `projects` 数组末尾追加完整对象：

```yaml
projects:
  - title: 项目名称
    period: 2026.07 - 至今
    role: 负责人 / 全栈开发
    summary: 一句话说明项目解决的问题和本人工作。
    outcomes:
      - 成果一
      - 成果二
```

字段均为必填。项目按文件中的顺序展示；要调整顺序，移动整个对象。每条成果以 `-` 开头。

### 修改教育和奖项

教育信息位于 `education`：

```yaml
education:
  school: 学校名称
  major: 专业名称
  period: 2024.09 - 至今
  courses: 课程一、课程二
```

奖项位于 `awards`，添加方法与技能相同：

```yaml
awards:
  - 新奖项名称
```

## 3. 每日一景接口

配置文件：`data/daily.yaml`

图片目录：`static/images/daily/`

```yaml
label: SAKURA · 01
image: images/daily/sakura-overlook.webp
alt: 樱色天空下眺望城市的狐狸娘
caption: 春风有信，花开有期。
```

| 字段 | 必填 | 用途 |
| --- | --- | --- |
| `label` | 是 | 每日一景右上角编号或日期 |
| `image` | 是 | 图片路径，必须以 `images/daily/` 开头 |
| `alt` | 是 | 无障碍替代文本，应描述图片内容 |
| `caption` | 是 | 图片下方短句 |

替换步骤：

1. 把新图片放进 `static/images/daily/`，例如 `2026-07-14.jpg`。
2. 修改 `image` 为 `images/daily/2026-07-14.jpg`。
3. 同步修改 `label`、`alt` 和 `caption`。
4. 不要修改 `profile.yaml` 的 `hero_art`，两者已经解耦。

## 4. 博客文章接口

文章目录：`content/posts/`

新建文章：

```bash
hugo new posts/my-new-post.md
```

文章格式：

```markdown
---
title: "文章标题"
date: 2026-07-13
tags: ["AI Agent", "Hugo"]
summary: "显示在首页文章卡片中的摘要。"
draft: false
---

这里开始写正文。

## 二级标题

正文支持列表、表格、引用、代码块、图片和链接。
```

| 字段 | 必填 | 用途 |
| --- | --- | --- |
| `title` | 是 | 文章标题 |
| `date` | 是 | 排序和显示日期，格式为 `YYYY-MM-DD` |
| `tags` | 建议 | 标签数组 |
| `summary` | 是 | 首页和列表页摘要 |
| `draft` | 否 | `true` 时生产构建不会发布 |

首页文章按日期倒序显示前 3 篇。全部文章位于 `/posts/`。

### 在文章中添加图片

1. 图片放入 `static/images/posts/`。
2. Markdown 中引用：

```markdown
![图片说明](/images/posts/example.jpg "可选图片标题")
```

部署在项目子路径时，本站的 Hugo 渲染模板会自动补全 `/MyBlog/` 前缀。

## 5. 友情链接接口

文件：`data/friends.yaml`

每个链接包含 4 个必填字段：

```yaml
- name: 站点名称
  url: https://example.com/
  description: 站点简介。
  tag: Blog
```

添加步骤：

1. 在文件末尾追加上述对象。
2. `url` 必须包含 `https://`。
3. `tag` 建议使用 `Blog`、`Code`、`Site` 或 `Campus`。
4. 首页右栏按 YAML 顺序展示。

点击时会立即播放 360ms 反馈动画，并按浏览器原生方式在新标签页打开；`Ctrl/Cmd + 点击` 等组合操作也保持原生行为。

## 6. 导航与首页顺序接口

左侧导航文件：`layouts/partials/home-sidebar.html`

中间内容顺序文件：`layouts/index.html`

当前顺序：

```text
左栏个人导航 | 中栏：封面 -> 最近文章 -> 项目经历 | 右栏：每日一景 -> About Me -> 友情链接
```

中栏每个模块对应一个 partial：

```go-html-template
{{ partial "hero.html" . }}
{{ partial "posts.html" . }}
{{ partial "projects.html" . }}
```

调整模块顺序时移动整行，同时更新 `posts.html`、`projects.html` 标题前的章节编号。左栏锚点必须与模块的 `id` 一致：`#posts`、`#projects`、`#friends`、`#about`。

## 7. 页面样式接口

主样式文件：`assets/css/main.css`

常用变量位于文件顶部：

```css
:root {
  --paper: #fffafd;
  --canvas: #fff0f6;
  --sakura: #ff7eb6;
  --vermilion: #c93676;
  --line: #4c2944;
  --corner: 2px;
}
```

修改颜色优先调整变量，不要逐个替换组件颜色。所有方框使用 `--corner` 作为圆角。首页模板样式位于 `/* Sakura dashboard home */` 注释之后。

## 8. 本地验证接口

开发预览：

```bash
hugo server -D
```

生产构建：

```bash
hugo --gc --minify --cleanDestinationDir --panicOnWarning
```

常见问题：

- 图片不显示：检查文件是否位于 `static/`，配置路径不要写 `static/` 前缀。
- GitHub Pages 路径错误：内部链接和模板图片应使用 `relURL`，Markdown 图片由渲染模板处理。
- 新文章不显示：检查 `draft` 是否为 `true`，日期是否有效，文件是否在 `content/posts/`。
- YAML 构建失败：检查缩进；数组项使用两个空格缩进并以 `-` 开头。

## 9. GitHub Pages 发布接口

工作流：`.github/workflows/hugo.yml`

发布流程：

1. 提交并推送工作流监听的分支。
2. GitHub Actions 执行 Hugo 生产构建。
3. 构建结果发布到 `gh-pages` 分支。
4. GitHub `Settings -> Pages` 保持 `Deploy from a branch`、`gh-pages`、`/ (root)`。
5. 等待部署完成后访问 `https://zx539.github.io/MyBlog/`。

不要手工修改 `public/`，它是构建产物并已被 `.gitignore` 忽略。
