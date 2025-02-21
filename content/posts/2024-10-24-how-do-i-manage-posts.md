+++
title = "How Do I Manage Posts on This Blog"
date = 2024-10-24T11:55:46+08:00
updated = 2024-10-25T22:20:00+08:00

[taxonomies]
tags = ["Blog", "Cloudflare", "GitHub", "Zola"]
+++

This post will describe how I manage the deployment of my blog.
The article will focus on how to deploy, and I will biefly touch on how to create a [Zola] blog.
The management solution is also applicable to other blog systems such as Hexo, Hugo, etc.

<!-- more -->

### Prepare the blog

I initialized the system through Zola CLI and installed a theme.
Now, just like other blog system, we only need one command ot generate static files for the entire site. Here is mine below:

```bash
zola build
```

It builds the entire site the `public` directory. Generally speaking, the distribution directory is ignored in `.gitignore`.

### Use `gh-pages` to deliver to a specific branch

The [gh-pages] is CLI helper to publish files to a `gh-pages` branch on GitHub (or any other branch anywhere else).

In my case, I created an extra empty `package.json` file as a workaround for [tschaub/gh-pages#354].
Then run the command below:

```bash
# Workaround for https://github.com/tschaub/gh-pages/issues/354
touch package.json

# Publish
gh-pages -d public
```

This will push all codes under the `public` directory to a `gh-pages` branch. GitHub will also enable the [GitHub Pages] for your repository.

At this point you can access your blog using your GitHub Pages domain.

### Boost with Cloudflare

GitHub Pages' domain does not have a good CDN function. At this time, we can consider using [Cloudflare] to improve the performance of the site.

Please note not to use the GitHub Pages custom domain directly. We don't need to bind the domain to GitHub Pages.
Cloudflare proxied domain bind to GitHub Pages will also cause the domain certificate to fail to renew correctly.
Instead, we chose to use [Cloudflare Pages] directly.

Here are the steps:

1. Go to your repository settings, set the GitHub Pages branch to "None"
1. Go to your Works & Pages Overview page, create a Pages app
1. Select the "Connect to Git", authorize with your GitHub account, then you will be able to select your repository from the list
1. Set the production branch to "gh-pages", and set the preview branch to "None"
1. Choose a domain for your Cloudflare Pages
1. Done, enjoy your blog

### Maintain the blog in a simple workflow

Here is my daily command to manage the blog sytem:

```bash
# Generate the static build
zola build

# Publish to `gh-pages` branch
gh-pages -d public
```

### Want a simpler deployment workflow?

Conguratulations on getting here. You can also follow the [Cloudflare Pages guide for Zola] to make your deployment to a simple `git push`.

The only thing to note is that you need to change the deployment version to 1. It is because the Zola is no longer supported on build system 2.

Remember to change the production branch from `gh-pages` back to `main` in the meantime.

### Links

- [Cloudflare]
- [Cloudflare Pages]
- [Cloudflare Pages guide for Zola]
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
