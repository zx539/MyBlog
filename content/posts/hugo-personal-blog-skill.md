---
title: "把个人博客经验整理成一个 Hugo Skill"
date: 2026-07-14
tags: ["Hugo", "Codex Skill", "GitHub Pages", "Markdown"]
summary: "从模块化内容、Markdown 渲染、媒体交互到 GitHub Pages 部署，把这次个人博客实践整理成可复用的 Codex Skill。"
draft: false
---

这次博客改造不只是换了一套界面。我把个人资料、项目、技能、友情链接、每日图片、文章、视频背景和部署流程拆成了独立模块，并把过程中遇到的问题整理成一个可以复用的 Codex Skill：`hugo-personal-blog`。

[下载 hugo-personal-blog Skill](/files/hugo-personal-blog-skill.zip)

## 为什么要把博客做成 Skill

个人博客的难点通常不在于写出一个首页，而在于后续维护：

- 新文章能否只写 Markdown；
- 个人信息和项目是否需要修改模板；
- 图片在本地正常，部署到项目子路径后是否仍能显示；
- 视频、动画和插件是否影响移动端与无障碍体验；
- GitHub Actions 能否稳定清理并发布旧页面。

Skill 的作用，是把这些容易遗漏的工程步骤变成固定工作流。下次创建或改造 Hugo 博客时，Codex 可以先读取 Skill，再按同一套质量门槛执行。

## 模块化内容接口

这套博客把作者经常修改的内容与页面实现分开：

| 内容 | 文件 |
| --- | --- |
| 昵称、签名、联系方式 | `data/profile.yaml` |
| 技能和项目经历 | `data/profile.yaml` |
| 友情链接 | `data/friends.yaml` |
| 每日一景 | `data/daily.yaml` |
| 博客文章 | `content/posts/*.md` |
| 图片与视频 | `static/images/`、`static/media/` |

以后增加项目，只需要在 YAML 数组末尾添加一个对象；增加文章，只需要新建 Markdown 文件。模板负责读取数据，不再重复硬编码内容。

## 完整 Markdown 渲染

文章由 Hugo Goldmark 渲染，并启用了表格、任务列表、定义列表、脚注、删除线和标题 ID。

```toml
[markup]
  [markup.goldmark.extensions]
    definitionList = true
    footnote = true
    strikethrough = true
    table = true
    taskList = true
```

Skill 要求文章页完整处理标题、列表、引用、行内代码、代码块、表格、图片、脚注和相邻文章，而不是只给普通段落添加样式。

### GitHub Pages 子路径

项目站点地址通常是：

```text
https://USER.github.io/REPO/
```

如果 Markdown 图片写成 `/images/example.jpg`，浏览器会请求域名根目录，丢失 `/REPO/`。因此 Skill 使用 Hugo render hook：先去掉开头的 `/`，再通过 `relURL` 补回仓库路径。

```go-html-template
{{- $destination = strings.TrimPrefix "/" $destination -}}
{{- $destination = $destination | relURL -}}
```

## 图片、视频与交互

当前博客支持静态 WebP 封面和循环 MP4 背景。装饰视频必须满足：

- `autoplay muted loop playsinline`；
- 有静态 poster；
- 提供播放和暂停控制；
- 在 `prefers-reduced-motion` 下关闭；
- 使用透明纸张层保证正文可读。

狐狸娘封面上的水波纹使用 Pointer Events 生成短生命周期节点，并限制触发频率，避免鼠标移动时创建过多 DOM。

## GitHub Pages 自动部署

工作流只提交源码，GitHub Actions 负责生成 `public/` 并发布到 `gh-pages`：

```bash
hugo --gc --minify --cleanDestinationDir --panicOnWarning
```

`--cleanDestinationDir` 很重要。删除文章或简历后，它能避免旧页面继续残留在部署分支。

## Skill 的使用方式

将下载后的目录解压到 `$CODEX_HOME/skills/hugo-personal-blog/`，然后在 Codex 中使用：

```text
使用 $hugo-personal-blog 帮我创建一个可部署到 GitHub Pages 的模块化个人博客。
```

也可以让它处理现有站点：

```text
使用 $hugo-personal-blog 检查我的 Markdown 渲染、项目子路径和 GitHub Pages 工作流。
```

Skill 内置检查脚本：

```bash
bash skills/hugo-personal-blog/scripts/check_hugo_blog.sh .
```

它会执行 Hugo 严格构建，并检查生成页面中是否还存在会破坏 GitHub Pages 项目路径的链接。

## 最终原则

一个能长期使用的个人博客，应当让写作比改模板更简单，让内容比样式更稳定，让部署比手工复制更可靠。

这也是这个 Skill 固化的核心：**数据模块化、Markdown 完整、路径可靠、媒体可降级、部署可验证。**
