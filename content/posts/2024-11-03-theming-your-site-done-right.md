+++
title = "Theming your site done right"
date = 2024-11-03T17:19:03+08:00

[taxonomies]
tags = ["CSS", "Front-End"]
+++

Nowadays, operating systems have the [light-on-dark color scheme] feature, and websites also have their own dark mode settings.
They provide three options of `Light`, `Dark` and `Sytem` for users to choose from.
So what are the potential problems?

<!-- more -->

Regarding the dark mode settings, our common undertand is that the website settings will take precedence over the system settings,
that is, when the website selects `Dark` even if the sytem is in `Light`, the website will still be displayed in `Dark`.

### How do developers maintain color themes?

Developers ussually use CSS to control different color themes, which can be roughly divded into the following two types.

#### 1. Manage with class name

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
const element = document.querySelector(".container");
element.classList.add("dark"); // Use dark mode
element.classList.remove("dark"); // Use light mode
```

This method makes it difficult to obtain the user's system themem, and switching the system theme cannot automatically update the CSS name for the page.
Because the system theme cannot re-trigger your JavaScript code.

#### 2. Manage with `prefers-color-scheme`

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

This way you can make your website support `Light`, `Dark` and `System` schemes.
This also avoided some potential scheme issue from other element.

### Common issues

The theme of my blog [litomore.me](/) is dark mode only.
But we still need to specify the `color-sheme: only dark` to forbids the user agent from overriding the color scheme for the page.
Like the npm site is a light theme only, but they didn't specify the `color-scheme` at the root level.
So those dual-theme images cannot be displayed correctly.
I've reported the bug to them at [org/community#discussions-61789].

And some developers define `prefers-ecolor-scheme` styles in child elements.
This means above problems may still occur in elements that do not have a defined color scheme.

### End

Congrats on reading this far. Do you know that you can also use the `prefers-color-scheme` in SVG images?
My blog [favicon] is using the dual-theme SVG. You can try switching the system theme to see its effect.

### Links

- [Light-on-dark color scheme]
- [CSS `prefer-color-scheme`][prefers-color-scheme]
- [CSS `color-scheme`][color-scheme]
- [org/community#discussions-61789]

[light-on-dark color scheme]: https://en.wikipedia.org/wiki/Light-on-dark_color_scheme
[prefers-color-scheme]: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme
[color-scheme]: https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme
[org/community#discussions-61789]: https://github.com/orgs/community/discussions/61789
[favicon]: https://litomore.me/favicon.svg