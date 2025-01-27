+++
title = "如何正确配置网站的白天和夜间模式"
date = 2024-11-03T17:19:03+08:00
draft = true

[taxonomies]
tags = ["CSS", "Front-End"]

[extra]
en_url = "/posts/theming-your-site-done-right/"
+++

现在的操作系统基本上都有了[夜间模式][light-on-dark color scheme]的功能，以及有些网站也有他们自己的夜间模式的相关设置。
一般他们都会提供`白天`、`夜间`以及`跟随系统`供用户选择。
那么这两种方式他们有什么潜在的问题吗？

<!-- more -->

按照我们对夜间模式的通常理解，如果你在网站上选择了夜间模式，那么它将覆盖你在系统选项里的设置。

### How do developers maintain color themes?

Developers ussually use CSS to control different color themes, which can be roughly divded into the following two types.

#### 1. Maintain with class name

The class name `.dark` solution requires the code to modify the CSS name every time user switch the theme. For example:

<!-- prettier-ignore-start -->
```css
.dark { color: #fff; }
```
<!-- prettier-ignore-end -->

```html
<div class="container dark" />
```

```js
container.classList.add("dark"); // Use dark mode
container.classList.remove("dark"); // Use light mode
```

This method makes it difficult to obtain the user's system theme, and switching the system theme cannot automatically update the CSS name for the page.
Because the system theme cannot re-trigger your JavaScript code.

#### 2. Maintain with `prefers-color-scheme`

The [prefers-color-scheme] is a more elegant solution. And your page theme can automatically change according to the changes of the sytem them.

<!-- prettier-ignore-start -->
```css
@media (prefers-color-scheme: dark) {
  .container { color: #fff; }
}
```
<!-- prettier-ignore-end -->

```html
<div class="container" />
```

Now you font color can be changed automatically according the system theme. But how to stick to a certain theme?

CSS has a [color-scheme] property for this situation. Here I use the inline style as example:

```html
<div class="container" style="color-scheme: only dark" />
```

```js
document.body.style.colorScheme = "only dark"; // Force dark mode
document.body.style.colorScheme = "only light"; // Force light mode
```

This way you can make your website support `Light`, `Dark` and `System` schemes.
This also avoided some potential scheme issue from other element.

But note the Safari does not support this feature on embedded resources due to [WebKit Bugzilla#199134].

### Common issues

The theme of my blog <a rel="noopener nofollow noreferrer" href="https://litomore.me">litomore.me</a> is dark mode only.
But we still need to specify the `color-sheme: only dark` to forbids the user agent from overriding the color scheme for the page.
Like the [npm] site is a light theme only, but they didn't specify the `color-scheme` at the root level.
So those dual-theme images cannot be displayed correctly.
I've reported the bug to them at [org/community#61789].

And some developers define `prefers-ecolor-scheme` styles in child elements.
This means above problems may still occur in elements that do not have a defined color scheme.

Coincidentally, [Notion] also has the same problem. I posted the problem on [this Notion page]. You can check it out if you are interested.

### End

Congrats on reading this far. Do you know that you can also use the `prefers-color-scheme` in SVG images?
My blog [favicon] is using the dual-theme SVG. You can try switching the system theme to see its effect.

My [Simple Icons CDN] also has a bunch of dual-theme supported icons. Feel free to check them out.

### Links

- [Light-on-dark color scheme]
- [CSS `prefer-color-scheme`][prefers-color-scheme]
- [CSS `color-scheme`][color-scheme]
- [WebKit Bugzilla#199134]
- [npm]
- [org/community#61789]
- [Notion]
- [Color scheme bug on Notion][Simple Icons CDN]
- [My favicon][favicon]
- [Simple Icons CDN]

[light-on-dark color scheme]: https://en.wikipedia.org/wiki/Light-on-dark_color_scheme
[prefers-color-scheme]: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme
[color-scheme]: https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme
[WebKit Bugzilla#199134]: https://bugs.webkit.org/show_bug.cgi?id=199134
[npm]: https://npmjs.com
[org/community#61789]: https://github.com/orgs/community/discussions/61789
[Notion]: https://notion.so
[this Notion page]: https://litomore.notion.site/The-page-icon-has-prefer-color-scheme-inside-416ec84944b043a1975fcce7f266349d
[favicon]: https://litomore.me/favicon.svg
[Simple Icons CDN]: https://github.com/LitoMore/simple-icons-cdn
