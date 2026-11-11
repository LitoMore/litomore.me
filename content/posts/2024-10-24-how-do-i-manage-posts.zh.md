+++
title = "我是如何管理这个博客的"
date = 2024-10-24T11:55:46+08:00
updated = 2024-10-25T22:20:00+08:00

[taxonomies]
tags = ["Blog", "Cloudflare", "GitHub", "Zola"]

[extra]
images = ["/og/posts/how-do-i-manage-posts.png"]
en_url = "/posts/how-do-i-manage-posts/"
+++

这篇文章会介绍我是如何管理博客部署的。
内容主要围绕部署展开，也会简单提一下如何创建一个 [Zola] 博客。
这套管理方式同样适用于 Hexo、Hugo 等其他博客系统。

<!-- more -->

### 准备博客

我先通过 Zola CLI 初始化博客，再安装一个主题。
和其他博客系统一样，现在只需要一条命令，就可以为整个网站生成静态文件。我的命令是：

```bash
zola build
```

这会把整个网站构建到 `public` 目录下。一般来说，这个构建产物目录会被添加到 `.gitignore` 中。

### 使用 `gh-pages` 发布到指定分支

[gh-pages] 是一个命令行工具，可以把文件发布到 GitHub 的 `gh-pages` 分支，也可以发布到其他仓库的其他分支。

我这里为了绕过 [tschaub/gh-pages#354]，额外创建了一个空的 `package.json` 文件。
然后运行以下命令：

```bash
# 绕过 https://github.com/tschaub/gh-pages/issues/354
touch package.json

# 发布
gh-pages -d public
```

这会把 `public` 目录下的所有文件推送到 `gh-pages` 分支。GitHub 也会为仓库启用 [GitHub Pages]。

到这里，你已经可以通过 GitHub Pages 域名访问博客了。

### 使用 Cloudflare 加速

GitHub Pages 域名的 CDN 表现不够理想，这时可以考虑用 [Cloudflare] 改善网站的访问体验。

注意，不要直接使用 GitHub Pages 的自定义域名功能。我们不需要把域名绑定到 GitHub Pages。
把开启 Cloudflare 代理的域名绑定到 GitHub Pages，还可能导致域名证书无法正常续期。
因此，我选择直接使用 [Cloudflare Pages]。

具体步骤如下：

1. 打开仓库设置，把 GitHub Pages 的分支设为「None」。
1. 进入 Workers & Pages 的概览页面，创建一个 Pages 应用。
1. 选择「Connect to Git」，授权 GitHub 账号，然后就可以在列表里选择对应仓库。
1. 把生产分支设为 `gh-pages`，预览分支设为「None」。
1. 为 Cloudflare Pages 选择一个域名。
1. 完成，可以开始使用博客了。

### 用简单的工作流维护博客

下面就是我日常管理博客时使用的命令：

```bash
# 生成静态文件
zola build

# 发布到 gh-pages 分支
gh-pages -d public
```

### 想要更简单的部署流程？

恭喜你读到这里。你也可以按照 [Cloudflare Pages 的 Zola 部署指南][Cloudflare Pages guide for Zola]，把部署简化成一次 `git push`。

唯一需要注意的是，要把构建系统版本改成 1，因为构建系统 2 已经不再内置支持 Zola。

同时记得把生产分支从 `gh-pages` 改回 `main`。

### 相关链接

- [Cloudflare]
- [Cloudflare Pages]
- [Cloudflare Pages 的 Zola 部署指南][Cloudflare Pages guide for Zola]
- [GitHub Pages]
- [Zola]
- [gh-pages]
- [tschaub/gh-pages#354]

[Cloudflare]: https://cloudflare.com
[Cloudflare Pages]: https://pages.cloudflare.com
[Cloudflare Pages guide for Zola]: https://developers.cloudflare.com/pages/framework-guides/deploy-a-zola-site/
[GitHub Pages]: https://pages.github.com
[Zola]: https://getzola.org
[gh-pages]: https://github.com/tschaub/gh-pages
[tschaub/gh-pages#354]: https://github.com/tschaub/gh-pages/issues/354
