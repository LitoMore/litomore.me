+++
title = "如何正确配置网站的白天和夜间模式"
date = 2024-11-03T17:19:03+08:00

[taxonomies]
tags = ["CSS", "Front-End"]

[extra]
images = ["/og/posts/theming-your-site-done-right.png"]
en_url = "/posts/theming-your-site-done-right/"
+++

现在的操作系统基本上都有了[夜间模式][light-on-dark color scheme]，很多网站也提供了自己的主题设置。
通常会有「白天」「夜间」和「跟随系统」三个选项。
那么，这些设置可能有哪些潜在问题呢？

<!-- more -->

按照通常的理解，网站的主题设置应该优先于系统设置。
也就是说，即使系统处于白天模式，只要在网站里选择了夜间模式，网站就应该保持夜间模式。

### 开发者如何管理颜色主题？

开发者通常使用 CSS 控制不同的颜色主题，大致可以分为以下两种方式。

#### 1. 通过类名管理

使用 `.dark` 类名的方案，需要在用户每次切换主题时，通过代码修改元素的 CSS 类名。例如：

<!-- prettier-ignore-start -->
```css
.dark { color: #fff; }
```
<!-- prettier-ignore-end -->

```html
<div class="container dark" />
```

```js
container.classList.add("dark"); // 使用夜间模式
container.classList.remove("dark"); // 使用白天模式
```

这种方式需要额外处理用户的系统主题，而且切换系统主题时，页面上的类名不会自动更新。
系统主题的变化不会自行重新执行这段 JavaScript。

#### 2. 通过 `prefers-color-scheme` 管理

[prefers-color-scheme] 是一种更优雅的方案，可以让页面主题自动跟随系统主题变化。

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

现在，文字颜色就可以随系统主题自动变化了。不过，如果想固定使用某种主题，该怎么办呢？

CSS 提供了 [color-scheme] 属性来处理颜色方案。这里用内联样式举例：

```html
<div class="container" style="color-scheme: only dark" />
```

```js
document.body.style.colorScheme = "only dark"; // 固定使用夜间模式
document.body.style.colorScheme = "only light"; // 固定使用白天模式
```

这样就可以让网站提供「白天」「夜间」和「跟随系统」三种方案。
同时，也能避免其他元素上可能出现的一些颜色方案问题。

不过，由于 [WebKit Bugzilla#199134]，Safari 对嵌入资源的相关支持还有问题。

### 常见问题

我的博客 <a rel="noopener nofollow noreferrer" href="https://litomore.me">litomore.me</a> 只有夜间模式。
即便如此，仍然需要指定 `color-scheme: only dark`，避免用户代理覆盖页面的颜色方案。
例如，[npm] 网站只有白天主题，却没有在根元素上指定 `color-scheme`。
这会导致支持双主题的图片无法正确显示。
我已经在 [org/community#61789] 向他们反馈了这个问题。

还有一些开发者只在子元素上定义 `prefers-color-scheme` 样式。
这意味着，没有明确指定颜色方案的元素仍然可能遇到上述问题。

巧的是，[Notion] 也有同样的问题。我把复现放在了[这个 Notion 页面][this Notion page]上，感兴趣的话可以看看。

### 最后

恭喜你读到这里。你知道 SVG 图片中也可以使用 `prefers-color-scheme` 吗？
我博客的 [favicon] 就是一个支持双主题的 SVG，可以试着切换系统主题，看看它的效果。

我的 [Simple Icons CDN] 也提供了很多支持双主题的图标，欢迎试用。

### 相关链接

- [夜间模式][light-on-dark color scheme]
- [CSS `prefer-color-scheme`][prefers-color-scheme]
- [CSS `color-scheme`][color-scheme]
- [WebKit Bugzilla#199134]
- [npm]
- [org/community#61789]
- [Notion]
- [Notion 上的颜色方案问题][this Notion page]
- [我的 favicon][favicon]
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
