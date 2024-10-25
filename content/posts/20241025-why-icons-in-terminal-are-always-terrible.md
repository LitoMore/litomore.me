+++
title = "Why icons in terminal are always terrible"
path = "why-icons-in-terminal-are-always-terrible"
date = 2024-10-25T22:26:00+08:00

[taxonomies]
tags = ["Font", "Icons", "Simple Icons", "Terminal"]
+++

Have you tried any terminal theme like [Powerlevel10k]? Or some funny prompts like [Starship]? Or some fonts like [Nerd Font] in terminals?
If you have experienced them, you may find that no matter which one of them, the icon font display experience is more or less unsatisfactory.

<!-- more -->

### What's the problem with icon font?

Let's simulate what would happen if the icon was displayed in the terminal (`case 1`):

![icon-cloudflare]
![icon-github]
![icon-go]

And even worse (`case 2`):`

![icon-cloudflare-worse]
![icon-github-worse]
![icon-go-worse]

Some icons look too small, don't they? Especially the Go icon.

And this might be what you expected (`case 3`):

![icon-cloudflare-expected]
![icon-github-expected]
![icon-go-expected]

This is because most icon fonts bound the icon entity to a squared viewbox. So why there is an "even worse"?

The answer is the character rendering of the termianl emulator. For these icon fonts, we generally call them `ambiguous characters`.

> Some characters, such as some Greek letters and Asian logograms, can take up either one or two cells in a terminal window.
> These characters are often referred to as ambiguous characters.
> By default, these characters are displayed with a narrow width in Terminal, which looks better in situations where perfect layout is important, such as in ASCII art.
> You can change your profile preferences to display ambiguous characters as wide, which can be better if you are reading running prose.
> (from: [GNOME Help - Characters look too narrow])

Some terminal emulators support justification for such characters.
For example, [iTerm2] has a checkbox "ambiguous characters are double-width" to adjust the rendering of the font.

What you see is `case 1` is double-width, while `case 2` treats your icon as a regular ASCII character.

### Is it possible rendering icons like `case 3`?

It's possible, but not exactly. To achieve such a display effect, we need to have a correctly produced font, they are no longer bounded in a squared viewbox.

Here I have built a preview in [simple-icons/simple-icons-font#211] that has fonts rendered with the same height at the same font size.

If you try the fonts I provided, you will find that almost all terminal emulators cannot render this preview font correctly.
This is because since I changed the viewbox of the icons, their width became unknown, the terminal emulator cannot automatically detect the width of the font, and it only supports regular width and double-width to render this font.

So why do say it still possible? The answer is the [Inline Images Protocol].
It's possible to use the [imgcat] tool to display images within terminal.
You may also need the [Simple Icons CDN] for colorable and customizable icons.

Here is an example:

<p align="center">
  <img width="465" src="https://raw.githubusercontent.com/LitoMore/simple-icons-cdn/main/media/imgcat-screenshot.webp" />
</p>

The `viewbox=auto` is to change the squared viewbox to the consistent viewbox in height. And the `size` is for rendering size.

But note this is not a solution for rendering icons in terminal, because the `imgcat -u` command is making a HTTP request to the remote.
It takes some time to download then render the icon. The performance is not good for terminals.
I had some topics at those terminal communities, and feel free to share your thoughts with them:

- [Starship] - Add support for Simple Icons ([starship/starship#6216])
- [Warp] - The fallback font for Warp ([warpdotdev/Warp#789#issuecomment-2351406819])
- [WezTerm] - Re-consider SVG support for imgcat ([wez/wezterm#6042])
- [WezTerm] - A brand new approach to icon fonts ([wez/wezterm/discussions#643])

### Expectations for the future of terminals

I will learn the relevant knowledge of the terminal and try to understand its principles and development in depth.
Of course, the development of the community also requires your actively participate in discussions and feedbacks.

Maybe one day, we can use inline font icons in terminals like this: ![icon-cloudflare-inline] ![icon-github-inline] ![icon-go-inline].

### Links

- [GNOME Help - Characters look too narrow]
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
