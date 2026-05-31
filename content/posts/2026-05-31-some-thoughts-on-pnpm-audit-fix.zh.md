+++
title = "一次 pnpm audit --fix 的小发现"
date = "2026-05-31T00:00:00+08:00"

[taxonomies]
tags = ["pnpm", "Security"]

[extra]
en_url = "/posts/some-thoughts-on-pnpm-audit-fix/"
+++

最近我们的项目升级了 [pnpm 11](https://pnpm.io/blog/releases/11.0)，在维护项目依赖的时候我看了下 `pnpm audit --fix` 会怎么修漏洞。`pnpm audit` 本身很好理解，它会检查 lockfile 里的依赖是否命中了已知漏洞。但到了执行 `--fix` 这一步，事情就开始变得有点微妙了。

<!-- more -->

我原本以为它会直接把依赖树更新到安全版本。实际看下来，pnpm 默认做的是另一件事：`pnpm audit --fix` 等价于 `pnpm audit --fix=override`，它会把修复版本写进 `pnpm-workspace.yaml` 的 `overrides`，然后让下一次 `pnpm install` 应用这个解析规则。不过这其实挺符合 pnpm 的思路。很多漏洞出现在 transitive dependencies 里，你不一定能直接修改上游依赖的 `package.json`。这个时候用 `overrides` 表达“这个范围不能再解析到脆弱版本”，会比强行改某个直接依赖更稳。但它也有一个很明显的副作用：这条规则会留在项目配置里，之后每一次 install 都会继续受它影响。

后来我又看了 `pnpm audit --fix=update`。这个模式更接近“把当前结果修掉”：它会尝试更新 vulnerable packages，让 lockfile 里的版本离开受影响范围，必要时也会更新直接依赖声明。和 `override` 比起来，`update` 留下的配置负担更少，但它也不一定能修掉所有漏洞。如果依赖关系卡住了，或者 advisory 没有可用的 patched range，它就只能留下 remaining vulnerabilities。所以这两个模式并不是「保守」和「激进」的区别，而是一个改规则，一个改结果。`override` 解决的是以后怎么解析，`update` 解决的是现在 lockfile 里是什么。

如果一个 hybrid 模式呢：先 update，修不掉的再 override。听起来很合理，但越想越觉得它不好定义。如果 update 只修掉一部分路径，报告应该怎么算？如果后面自动写了 override，下一次运行要不要试着删掉？如果用户本来就写了自己的 override，pnpm 又怎么知道哪一条是 audit 生成的？也许正是因为这些边界不清楚，pnpm 现在把两个模式分开。你可以先跑 `pnpm audit --fix=update`，如果还有剩余问题，再决定要不要跑默认的 `pnpm audit --fix`。这没有那么自动化，但副作用至少是清楚的。

另一个有意思的地方是 `minimumReleaseAge`。pnpm v11 把它的默认值改成了 `1440`，也就是新发布的版本需要等一天才会被解析到。这个设置是为了 supply chain security，避免项目马上装到刚发布、还没来得及被社区发现问题的版本。但安全补丁也经常是刚发布的。于是 `audit --fix` 会遇到一个矛盾：patched version 是安全修复，但它可能还没满足 `minimumReleaseAge`。pnpm 的处理方式是，当 `minimumReleaseAge` 生效时，`pnpm audit --fix` 和 `pnpm audit --fix=update` 会把每个 advisory 的最小 patched version 加到 `minimumReleaseAgeExclude`，让安全修复可以绕过 release age 窗口。

我觉得这个取舍是可以理解的。继续停留在已知 vulnerable version 是确定风险，而刚发布的 patched version 是潜在风险。pnpm 在这里选择先处理确定风险。但这个设计留下了一个维护问题。`minimumReleaseAgeExclude` 里的 exact version 通常只在短时间内有用。等这个版本已经发布超过一天，它本来就满足 `minimumReleaseAge` 了，对应的 exclude 就不再必要。可是 pnpm 现在不会自动清理它。

这也是我提 [pnpm/pnpm#11668](https://github.com/pnpm/pnpm/issues/11668) 的原因。长期使用 `pnpm audit --fix` 或 `pnpm audit --fix=update`，`minimumReleaseAgeExclude` 会不断追加版本。它们当时是有意义的，但过了 release age 窗口后就变成了配置里的历史记录。半年后再看 `pnpm-workspace.yaml`，你很难判断某条 exclude 是 audit 自动加的、维护者手动加的，还是早就可以删了。自动清理看起来简单，但实际也有成本。pnpm 需要知道版本发布时间，这可能要读取 registry metadata；它还需要避免误删用户手写的 exact version。所以我更倾向于未来有一个显式的 cleanup 机制，而不是让 `audit --fix` 或 `install` 在背后偷偷清理。

最后我的维护流程大概会是这样：想尽量少留下长期配置，就先试 `pnpm audit --fix=update`；如果 update 修不掉，再考虑默认的 `pnpm audit --fix`。但只要项目里开了 `minimumReleaseAge`，我都会多看一眼 `pnpm-workspace.yaml`，因为 `overrides` 和 `minimumReleaseAgeExclude` 都不是一次性的日志，它们会继续影响之后的 install。

分析下来我会觉得 pnpm 11 的每个功能模块之间有些割裂，虽然上了很多不错的功能，但到了实际开发情境下又显得不太得劲儿。接下来我应该会尝试给 pnpm 提一版代码，沿着 [pnpm/pnpm#11668](https://github.com/pnpm/pnpm/issues/11668) 里提到的方向优化这块体验。比起让 `audit --fix` 或 `install` 自动做太多事情，我更想先尝试一个显式的维护入口，比如增加一个 `pnpm clean` 命令，专门用来清理这类已经不再需要的 `minimumReleaseAgeExclude` 条目。这样清理动作是可预期的，也不会和安全修复本身混在一起。

## Links

- [pnpm audit](https://pnpm.io/cli/audit)
- [minimumReleaseAge](https://pnpm.io/settings#minimumreleaseage)
- [minimumReleaseAgeExclude](https://pnpm.io/settings#minimumreleaseageexclude)
- [pnpm#11668](https://github.com/pnpm/pnpm/issues/11668)
