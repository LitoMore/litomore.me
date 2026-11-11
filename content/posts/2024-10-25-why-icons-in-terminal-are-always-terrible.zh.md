+++
title = "为什么终端里的图标总是显示不好"
date = 2024-10-25T22:26:00+08:00

[taxonomies]
tags = ["Font", "Icons", "Simple Icons", "Terminal"]

[extra]
images = ["/og/posts/why-icons-in-terminal-are-always-terrible.png"]
en_url = "/posts/why-icons-in-terminal-are-always-terrible/"
+++

你有没有试过 [Powerlevel10k] 这样的终端主题、[Starship] 这样的命令行提示工具，或者在终端里使用 [Nerd Font] 之类的字体？
如果用过，你可能会发现，不管用哪一种，图标字体的显示体验总有些不尽如人意。

<!-- more -->

### 图标字体有什么问题？

先模拟一下图标在终端中显示时的样子（`情况 1`）：

![icon-cloudflare]
![icon-github]
![icon-go]

甚至还可能更糟（`情况 2`）：

![icon-cloudflare-worse]
![icon-github-worse]
![icon-go-worse]

有些图标是不是看起来太小了？尤其是 Go 的图标。

而你期待的可能是这样（`情况 3`）：

![icon-cloudflare-expected]
![icon-github-expected]
![icon-go-expected]

这是因为大多数图标字体都把图标放进了一个正方形的 viewbox 里。那么，为什么还会出现「更糟」的情况呢？

答案在于终端模拟器对字符的渲染方式。这类图标字体中的字符，通常会被归为 `ambiguous characters`，也就是宽度不明确的字符。

> 有些字符，例如部分希腊字母和亚洲文字，在终端窗口中既可以占一个单元格，也可以占两个单元格。
> 这类字符通常被称为宽度不明确的字符。
> 默认情况下，终端会以窄字符显示它们，这样在 ASCII 艺术等对排版要求严格的场景里效果更好。
> 你可以在配置偏好中把它们设为宽字符，这在阅读连续文本时可能更合适。
> （来源：[GNOME 帮助：字符看起来太窄][GNOME Help - Characters look too narrow]）

有些终端模拟器支持调整这类字符的宽度。
比如，[iTerm2] 就有一个「ambiguous characters are double-width」选项，用来调整字体的渲染方式。

`情况 1` 是按双宽字符显示的效果，而 `情况 2` 则把图标当成了普通 ASCII 字符。

### 能不能像 `情况 3` 那样显示图标？

可以，但也不完全可以。要实现这样的效果，首先需要一套制作方式正确的字体，让图标不再受限于正方形的 viewbox。

我在 [simple-icons/simple-icons-font#211] 里做了一套预览字体，让所有图标在相同字号下具有一致的高度。

如果试用这套字体，你会发现几乎所有终端模拟器都无法正确显示它。
这是因为修改图标的 viewbox 后，字符宽度就不再固定，而终端模拟器无法自动判断它的宽度，只支持用普通字符宽度或双宽来渲染。

那为什么又说可以呢？答案是 [Inline Images Protocol]。
我们可以使用 [imgcat] 工具，直接在终端里显示图片。
你可能还需要 [Simple Icons CDN]，来获取可以调整颜色和尺寸的图标。

下面是一个例子：

<p align="center">
  <img width="465" src="https://raw.githubusercontent.com/LitoMore/simple-icons-cdn/main/media/imgcat-screenshot.webp" />
</p>

其中，`viewbox=auto` 用来把正方形 viewbox 改为高度一致的 viewbox，`size` 则用于控制渲染尺寸。

不过，这还算不上在终端中渲染图标的解决方案。因为 `imgcat -u` 会向远程服务器发送 HTTP 请求，下载图标后才能显示，性能并不适合终端提示符。
我在几个终端社区里发起过相关讨论，也欢迎你去分享想法：

- [Starship]：添加对 Simple Icons 的支持（[starship/starship#6216]）
- [Warp]：Warp 的后备字体（[warpdotdev/Warp#789#issuecomment-2351406819]）
- [WezTerm]：重新考虑为 imgcat 提供 SVG 支持（[wez/wezterm#6042]）
- [WezTerm]：一种全新的图标字体方案（[wez/wezterm/discussions#643]）

### 对终端未来的期待

我准备学习一些终端相关的知识，试着深入了解它的原理和开发。
当然，社区的发展也需要大家积极参与讨论和反馈。

也许有一天，我们就能在终端里用上这样的行内字体图标：![icon-cloudflare-inline] ![icon-github-inline] ![icon-go-inline]。

### 相关链接

- [GNOME 帮助：字符看起来太窄][GNOME Help - Characters look too narrow]
- [Inline Images Protocol]
- [Nerd Font]
- [Powerlevel10k]
- [Simple Icons CDN]
- [Starship]
- [Warp]
- [WezTerm]
- [imgcat]
- [iTerm2]
- [simple-icons/simple-icons-font#211]
- [starship/starship#6216]
- [wez/wezterm#6042]
- [wez/wezterm/discussions#643]
- [warpdotdev/Warp#789#issuecomment-2351406819]

[GNOME Help - Characters look too narrow]: https://help.gnome.org/users/gnome-terminal/stable/pref-profile-char-width.html.en
[Inline Images Protocol]: https://iterm2.com/documentation-images.html
[Nerd Font]: https://www.nerdfonts.com
[Powerlevel10k]: https://github.com/romkatv/powerlevel10k
[Simple Icons CDN]: https://github.com/LitoMore/simple-icons-cdn
[Starship]: https://starship.rs
[Warp]: https://warp.dev
[WezTerm]: https://wezfurlong.org/wezterm/
[imgcat]: https://iterm2.com/utilities/imgcat
[iTerm2]: https://iterm2.com
[simple-icons/simple-icons-font#211]: https://github.com/simple-icons/simple-icons-font/issues/211
[starship/starship#6216]: https://github.com/starship/starship/issues/6216
[warpdotdev/Warp#789#issuecomment-2351406819]: https://github.com/warpdotdev/Warp/issues/789#issuecomment-2351406819
[wez/wezterm]: https://github.com/wez/wezterm
[wez/wezterm#6042]: https://github.com/wez/wezterm/issues/6042
[wez/wezterm/discussions#643]: https://github.com/wez/wezterm/discussions/6143
[icon-cloudflare]: https://cdn.simpleicons.org/cloudflare/999?size=20
[icon-cloudflare-worse]: https://cdn.simpleicons.org/cloudflare/999?size=10
[icon-cloudflare-inline]: https://cdn.simpleicons.org/cloudflare?viewbox=auto&size=14
[icon-cloudflare-expected]: https://cdn.simpleicons.org/cloudflare/999?viewbox=auto&size=20
[icon-github]: https://cdn.simpleicons.org/github/999?size=20
[icon-github-worse]: https://cdn.simpleicons.org/github/999?size=10
[icon-github-inline]: https://cdn.simpleicons.org/github/eaeaea?viewbox=auto&size=14
[icon-github-expected]: https://cdn.simpleicons.org/github/999?viewbox=auto&size=20
[icon-go]: https://cdn.simpleicons.org/go/999?size=20
[icon-go-worse]: https://cdn.simpleicons.org/go/999?size=10
[icon-go-inline]: https://cdn.simpleicons.org/go?viewbox=auto&size=14
[icon-go-expected]: https://cdn.simpleicons.org/go/999?viewbox=auto&size=20
