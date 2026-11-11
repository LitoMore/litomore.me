+++
title = "PS Remote Play 使用中的一些问题"
date = 2024-10-28T11:30:00+08:00

[taxonomies]
tags = ["Devices", "Gaming", "PlayStation", "PS Remote Play"]

[extra]
images = ["/og/posts/problems-with-ps-remote-play.png"]
en_url = "/posts/problems-with-ps-remote-play/"
+++

我已经用了一段时间的 [PS Remote Play]，也试过不少设备组合，包括 iPhone 搭配 [Backbone One]、Steam Deck 上的 [Chiaki4Deck]、Mac 搭配 [DualSense®]，以及 [PlayStation Portal™]。
用它玩过不少游戏之后，我觉得是时候分享一下自己的体验了。

<!-- more -->

我猜很多人第一次接触 PS Remote Play，都是通过官方应用。
这种情况下，大家通常不会另外准备一个手柄。
当然，也可以把手柄连接到设备上，但这样就失去了手机和平板原本的便携性。
这篇文章就不展开讲最基础的使用体验了，主要分享我自己玩 PS Remote Play 的几种方式，以及它们各自的优缺点。

### Backbone One

我用的是 iPhone 搭配 [Backbone One 的 PlayStation® 版本][Backbone One - PlayStation® Edtion]。它解决了手机上只能使用触屏虚拟按键的问题。
在 iPhone 上，还可以通过系统内置设置[自定义游戏手柄按键][customize the game controller buttons]。

连接质量取决于手机和路由器。可以选择支持 Wi-Fi 6，甚至 Wi-Fi 7 的设备，尽量改善连接体验。

这样就能用上手机的高素质屏幕，甚至 HDR。只要屏幕支持，PS Remote Play 就可以输出 HDR 画面。

游戏体验则取决于你对这类手柄的适应程度。
除了 Backbone One，市面上还有 [LeadJoy]、[Razer Kishi] 等其他品牌的手机手柄可选。
但它们都有一个共同的问题：不支持触摸板。

触摸板是索尼游戏主机手柄上的一个特殊按键，不过我们可以用手机屏幕代替它。
真的是这样吗？实际体验是：

每次想使用触摸板，都必须先点一下手机屏幕，激活触摸板浮层，之后才能进行操作。
也就是说，要完成游戏里的一次触摸板点击，至少得点两下。
而且，屏幕上的触摸板位于中上方，正常握持手柄时几乎碰不到。

你可能会想：iPhone 不是可以重新映射按键吗？手柄上又有分享键，能不能把触摸板映射到分享键上？答案是不行。
至少 Backbone One 不支持。我联系过他们的客服，对方告诉我这些按键不能修改。

对于需要频繁使用触摸板的游戏，这就很不友好了。比如 [HELLDIVERS™ 2]，就需要用触摸板来开关地图。

### Steam Deck 上的 Chiaki4Deck

它的游戏体验和手机搭配手柄基本相同。
不过，既然用的是 Steam Deck，这次就可以把触摸板映射到 [L4、L5、R4、R5][L4 L5 R4 R5] 上。
缺点可能就是 Steam Deck 本身比较重，屏幕表现也一般。

### PC/Mac 搭配 DualSense®

这种方式和直接在主机上玩相比，主要区别就是延迟。如果你需要直播游戏，这也是一种节省采集卡开销的办法。

### PlayStation Portal™

终于说到大家可能最感兴趣的设备了。
你可能已经看过不少 PlayStation Portal™ 的评测视频，这里我挑几个重点聊聊。

首先，它最大的优点是拥有完整的 DualSense® 手柄功能，包括自适应扳机。
除了实体触摸板，它基本能提供使用 DualSense® 的全部体验。

和前面提到的一样，PlayStation Portal™ 的触摸板操作也需要通过触屏完成。
这次，屏幕左右两侧都会显示触摸板区域，用拇指就能轻松点到，不过仍然要点两下。

不太好的是，如果点错了触摸板的位置，整个屏幕都会被一层浮层覆盖，影响其他游戏操作。

可惜这台设备不支持 Wi-Fi 6 或更高版本。在我的体验里，这也意味着它至少会有 80ms 左右的延迟。

### 相关链接

- [Backbone One]
- [Backbone One 的 PlayStation® 版本][Backbone One - PlayStation® Edtion]
- [Chiaki4Deck]
- [自定义游戏手柄按键][customize the game controller buttons]
- [DualSense®]
- [HELLDIVERS™ 2]
- [L4、L5、R4、R5][L4 L5 R4 R5]
- [LeadJoy]
- [PS Remote Play]
- [PlayStation Portal™]
- [Razer Kishi]
- [Steam Deck]

### 相关文章

- [我的游戏设备](@/collections/gaming-devices.md)

[Backbone One]: https://backbone.com
[Backbone One - PlayStation® Edtion]: https://backbone.com/products/backbone-one-playstation/
[Chiaki4Deck]: https://github.com/streetpea/chiaki-ng
[customize the game controller buttons]: https://support.apple.com/en-mt/guide/iphone/iph9d38dd45f/ios
[DualSense®]: https://www.playstation.com/en-us/accessories/dualsense-wireless-controller/
[HELLDIVERS™ 2]: https://www.playstation.com/en-us/games/helldivers-2/
[L4 L5 R4 R5]: https://www.reddit.com/r/SteamDeck/comments/193pimg/how_to_map_buttons_on_back/
[LeadJoy]: https://leadjoy.top
[PS Remote Play]: https://www.playstation.com/en-us/remote-play/
[PlayStation Portal™]: https://www.playstation.com/en-us/accessories/playstation-portal-remote-player/?emcid=pa-co-513730&gad_source=1&gclid=CjwKCAjwyfe4BhAWEiwAkIL8sCBv_7IuIh5CN_q3wah1l83BwumKrAXybn0aHtZKC5llQhaztD14jRoC46UQAvD_BwE&gclsrc=aw.ds
[RAZER KISHI]: https://www.razer.com/hk-en/mobile-controllers/razer-kishi-v2
[Steam Deck]: https://store.steampowered.com/steamdeck/
