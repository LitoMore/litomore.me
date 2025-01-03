+++
title = "GitHub 2024 年度总结"
date = "2025-01-01T00:00:00+08:00"

[taxonomies]
tags = ["GitHub", "开源", "年度总结"]
+++

我的开源经历的第八年即将结束并迎来第九年。为此我手动统计了去年一年的数据并制定了一些奖项。让我们来看看都有什么吧！

<!-- more -->

## GitHub 贡献统计

2024 年是我年度贡献数量最多的一年，期间我在开源社区提交了 `1686` 次贡献，并且参加了一些新的 GitHub 组织，其中有
[@raycast](https://github.com/raycast),
[@denoland](https://github.com/denoland),
[@jsr-io](https://github.com/jsr-io),
[@lycheeverse](https://github.com/lycheeverse),
[@Crossbell-Box](https://githu.com/Crossbell-Box),
以及 GNOME 的 [@do-not-theme](https://github.com/do-not-theme).

![](/images/github-wrapped-2024.webp)

这一年，我也在尝试更多的领域：

- 我在 [Simple Icons Extreme](https://github.com/LitoMore/simple-icons-extreme) 项目首次尝试了 Bun 并投入使用
- 我用 Deno 重构了 [Simple Icons CDN](https://github.com/LitoMore/simple-icons-cdn) 并向 [Deno standard library](https://github.com/denoland/std) 贡献了代码
- 我创建了我的第一个私有 SwiftUI 项目，并实现了第一个 PoC 版本
- 我完成了我的第一个 Rust Wasm 项目，并用于个人项目
- 以及更多 ...

下一年我将会进行更加深入的学习，对此我已经有了相应的规划，也许我会在明年的 GitHub 年度总结里跟大家分享。

<!--

## Raycast Community

This year I used Raycast and its extensibility to develop a lot of tools to improve my work efficiency.

I also made a lot of new [Raycast extensions](https://github.com/raycast/extensions), here are some of them:

- [Badges](https://raycast.com/litomore/badges) - Concise, consistent, and legible badges
- [Brand Icons](https://raycast.com/litomore/simple-icons) - Browse, Search, and Copy 3200+ popular brand icons from Simple Icons
- [MapleStroy.gg](https://raycast.com/litomore/maplestory-gg) - MapleStory's Definitive Database
- [PM2](https://raycast.com/litomore/pm2) - Advanced, production process manager for Node.js
- [ProtonDB](https://raycast.com/litomore/protondb) - Browse game information for Proton, Linux, Steam Deck, and SteamOS
- [Raycast Port](https://raycast.com/litomore/raycast-port) - This allows you to use Raycast features out of Raycast
- [Say](https://raycast.com/litomore/say) - Use the macOS built-in TTS (Spoken Content) to say the text you provide
- [SteamGridDB](https://raycast.com/litomore/steamgriddb) - Download and share custom video game assets and personalize your gaming library
- [TourBox](https://raycast.com/litomore/tourbox) - Find Your Desired TourBox Preset
- [United Nations](https://raycast.com/litomore/united-nations) - Peace, dignity and equality on a healthy planet

And some extensions contributed by me:

- [Color Picker](https://raycast.com/thomas/color-picker) - Pick and organize colors, everywhere on your Mac
- [GitHub](https://raycast.com/raycast/github) - Work with GitHub on Raycast
- [Google Translate](https://raycast.com/gebeto/translate) - Simple translation using Google Translate
- [Pomodoro](https://raycast.com/asubbotin/pomodoro) - Pomodoro extension with menu-bar timer
- [Mastodon](https://raycast.com/SevicheCC/mastodon) - Publish status from Raycast to Mastodon, and view your bookmarked status
- [npm](https://github.com/mrmartineau/search-npm) - Search for npm package information
- [and more](https://raycast.com/litomore) ...

-->

## 奖项

这里我将提名一些我在 GitHub 经历的项目以及 issues 和 PRs。由于这是我的第一届年度总结，所以下面的提名里我会提名一些 2024 年以前的内容。

### 体验创新奖

> 这一年我花了一些点时间在尝试提升开发者和用户体验，这可能是是一些微不足道改进，也可能是一次对项目的重大提升。
> 但无论是哪一种它们都将你的体验升级到了一个新的阶段，并也有可能影响项目未来的发展。

提名名单：

- [badges/shields#9191](https://github.com/badges/shields/pull/9191) - 这个 PR 为 [shields.io](https://shields.io) 添加了自适应图标大小的功能，这可以让你的个人或项目介绍页面在使用较宽的图标的情况下也能保持整洁美观
- [LitoMore/raycast-cross-extension-conventions](https://github.com/LitoMore/raycast-cross-extension-conventions) - 它定义了 Ryacast 跨插件情景下的开发约定，并且 Raycast 的 CEO 也给这个项目标星了喔
- [Say - Text to Speech](https://raycast.com/litomore/say) - 这个 Raycast 插件使用 macOS 内置朗读功能来阅读你提供的文字，并且它支持使用 Siri 的声音来达到最佳的使用体验

那么，这一届的体验创新奖的冠军是……[badges/shields#9191](https://github.com/badges/shields/pull/9191)！这不仅仅是 shields.io 一次重大的改进，同时也是对整个开源社区体验的提升！

### 最荒诞奖

> 每当你无所顾虑地投入你的热情到一个项目里的时候，这个世界总会突然用一句「林子大了什么鸟都有」把你叫醒。
> 它让你发现原来开源社区也可以如此荒诞，也是它们，让你的开源经历变得如此有趣。

提名名单：

- [simple-icons/simple-icons#7970](https://github.com/simple-icons/simple-icons/issues/7970) - 此 issue 请求添加 `SaveWalterWhite.com` 到我们的图标库中
- [simple-icons/simple-icons#9316](https://github.com/simple-icons/simple-icons/pull/9316) - 此 PR 删除了可爱的 Bun 图标的眼睛，并让它看起来像个盲包子
- [simple-icons/simple-icons#12312](https://github.com/simple-icons/simple-icons/pull/12312) - 此 PR 作者抱怨我们的维护者不知道什么是 ePBF，并且说我们的根本不会写代码

那么，这一届的体验创新奖的冠军是……[simple-icons/simple-icons#12312](https://github.com/simple-icons/simple-icons/pull/12312)！啊？你问我为什么？这可是 ePBF！你写过代码么？

<!--

### Best Sponsorship Award

> As an open-sourcerer, I believe in the power of collaboration and the importance of giving back to the community.
> Your support not only helps me financially, but it also motivates me to continue working on these projects and making them better.

Nominations:

- [Frontend Masters](https://github.com/FrontendMasters) (Sponsor)
- [Roboflow](https://github.com/roboflow) (Sponsor)
- [Sevi.C](https://github.com/Sevichecc) (Sponsoring)

The winner is [Sevi.C](https://github.com/Sevichecc)! Congrats, and wish you great success in achieving your 2024 flags in 2025!

-->

## 结尾

以上就是这届 GitHub Wrapped 2024 全部内容了。我们明年再见。