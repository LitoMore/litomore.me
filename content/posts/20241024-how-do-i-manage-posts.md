+++
title = "How do I manage posts on this blog"
path = "posts/how-do-i-manage-posts"
date = 2024-10-24T11:55:46+08:00

[taxonomies]
tags = ["Blog", "Cloudflare", "GitHub", "Zola"]
+++

This post will describe how I manage the deployment of my blog.
The article will focus on how to deploy, and I will biefly touch on how to create a [Zola] blog.
The management solution is also applicable to other blog systems such as Hexo, Hugo, etc.

<!-- more -->

## Prepare the blog

I initialized the system through Zola CLI and installed a theme.
Now, just like other blog system, we only need one command ot generate static files for the entire site. Here is mine below:

```bash
zola build
```

It builds the entire site the `public` directory. Generally speaking, the distribution directory is ignored in `.gitignore`.

## Use `gh-pages` to deliver to a specific branch

The [gh-pages] is CLI helper to publish files to a `gh-pages` branch on GitHub (or any other branch anywhere else).

In my case, just simply run the command below:

```bash
gh-pages -d public
```

This will push all codes under the `public` directory to a `gh-pages` branch. GitHub will also enable the [GitHub Pages] for your repository.

At this point you can access your blog using your GitHub Pages domain.

## Boost with Cloudflare

GitHub Pages' domain does not have a good CDN function. At this time, we can consider using [Cloudflare] to improve the performance of the site.

Please note not to use the GitHub Pages custom domain directly. We don't need to bind the domain to GitHub Pages. Instead, we chose to use [Cloudflare Pages] directly.

Here are the steps:

1. Go to your repository settings, set the GitHub Pages branch to "None"
1. Go to your Works & Pages Overview page, create a Pages app
1. Select the "Connect to Git", authorize with your GitHub account, then you will be able to select your repository from the list
1. Set the production branch to "gh-pages", and set the preview branch to "None"
1. Choose a domain for your Cloudflare Pages
1. Done, enjoy your blog

## Maintain the blog in a simple workflow

Here is my daily command to manage the blog sytem:

```bash
# Generate the static build
zola build

# Publish to `gh-pages` branch
gh-pages -d public
```

You can also use the [GitHub Actions] to make your deployment to a simple `git push`.

Enjoy~

## Links

- [Cloudflare]
- [Cloudflare Pages]
- [gh-pages]
- [GitHub Actions]
- [GitHub Pages]
- [Zola]

[Cloudflare]: https://cloudflare.com
[Cloudflare Pages]: https://pages.cloudflare.com
[gh-pages]: https://github.com/tschaub/gh-pages
[GitHub Actions]: https://github.com/features/actions
[GitHub Pages]: https://pages.github.com
[Zola]: https://getzola.org
