---
layout: default
title: "GitHub Actions Marketplace"
permalink: /mynotes/github_marketplace.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# 将 action 发布到 GitHub Marketplace
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

本文以 [ThreadScale](https://github.com/gemc/ThreadScale) 为例：
其根目录中的 action 已发布为 [Marketplace 上的 ThreadScale](https://github.com/marketplace/actions/threadscale)，
各工作流通过 `uses: gemc/ThreadScale@v1` 调用它。

## 准备仓库

使用一个专门用于该 action 的公开仓库，并在其根目录放置一个 `action.yml` 或 `action.yaml`。
选择一个唯一的 action 名称，确保它不与 Marketplace 上已有的名称或 GitHub 的保留名称冲突。

ThreadScale 的元数据包含以下字段；其完整的 `action.yml` 还声明了输入和输出：

```yaml
name: ThreadScale
description: Measure strong scaling, speedup, throughput, and parallel efficiency across application threads.
author: GEMC Collaboration

branding:
  color: blue
  icon: activity

runs:
  using: node24
  main: src/main.js
```

对于你自己的 action，请替换名称、描述、品牌标识和入口点。仓库中应包含 `runs.main` 引用的代码、
说明用法和输入的 README，以及许可证。ThreadScale 使用 MIT 许可证，直接运行 JavaScript，
无需运行时依赖或构建步骤。其本地检查命令为：

```shell
npm run check
npm test
```

ThreadScale 还在 `.github/workflows/` 下提供了一个可复用工作流；其 Marketplace 条目来自
根目录中的 `action.yml`。

<br/>

## 通过 GitHub 发布

1. 在 GitHub 上打开仓库根目录的 `action.yml`，通过其中的发布横幅起草一个发布版本。
2. 在发布表单中勾选 Marketplace 发布复选框。
3. 如果该复选框被禁用，仓库所有者或组织所有者必须通过发布页面接受 Marketplace 开发者
   协议。发布还要求启用双重身份验证。
4. 解决所有元数据验证错误，然后选择一个主要类别，也可以选择第二个类别。
5. 为要发布的代码选择固定版本标签，然后添加发布标题和说明：
   - 如果要将已有的 `v1.0.0` 上架，请选择该标签。如果对应的 GitHub Release 已存在，请编辑
     该发布版本，并在其中启用 Marketplace 发布。
   - 如果要发布更新后的代码，请在经过测试的提交上创建或选择 `v1.0.1`。创建
     标签时，请确认发布目标是你测试过的提交。
   - 发布时使用固定版本标签；保留 `v1` 作为供使用者引用的移动标签。
6. 发布该版本，并检查生成的 Marketplace 条目。符合条件的 action 会立即显示，
   无需单独审核。

有关当前的要求和界面，请参阅 [GitHub 的发布说明][publishing]。

<br/>

## 维护版本标签

假设 `v1` 当前指向与 `v1.0.0` 相同的提交。将该已有版本发布到 Marketplace
不需要更改任何标签。无需仅为添加 Marketplace 条目而创建 `v1.0.1`。

当更新后的代码准备就绪时，发布一个关联到 `v1.0.1` 的新 GitHub Release，并启用 Marketplace
发布。然后将 `v1` 移动到与 `v1.0.1` 相同的提交。创建新发布版本时，这一步**不会**自动完成；
请自行更新标签，或配置发布自动化来完成此操作。

发布 `v1.0.1` 后，在你的 action 仓库中运行以下命令：

```shell
git fetch origin tag v1.0.1
git tag -f v1 'v1.0.1^{}'
git push --force origin refs/tags/v1
```

`^{}` 后缀将版本标签解析为其对应的提交。只有 `v1` 会移动；`v1.0.0`、`v1.0.1` 及其
GitHub Release 保留各自原本的目标。使用 `@v1` 的使用者会在后续运行中获得更新后的代码，
而使用 `@v1.0.0` 的使用者则继续使用该版本。详情请参阅 [关于发布标签的 Git 笔记][tags]。

ThreadScale 的可复用工作流内部也引用了 `gemc/ThreadScale@v1`，因此在使用者运行它之前，
该标签必须存在。用户可以选择 `@v1` 以获取兼容更新，也可以固定到某个完整的提交 SHA。

对于后续版本，请发布一个启用了 Marketplace 发布的新版本，然后针对兼容的更改更新
主版本标签。保留较早的版本标签。

<br/>

## 帮助人们发现并试用该 action

- 在 README 开头介绍它解决的问题，提供一个可运行的简短工作流，并展示结果截图。
  ThreadScale 的扩展性能图表就是一个值得展示的示例。
- 添加清晰的仓库描述、相关的主题标签，例如 `github-action`、`benchmark` 和
  `performance`，以及 Marketplace 链接。在你的主页和相关项目文档中添加该 action 的链接。
- 发布一篇使用真实应用的简短教程，包含其工作流和生成的报告。
  将教程分享给相关的科学计算社区和合作者，并发布到 LinkedIn 上。
- 如果符合收录范围，建议将其收录到有人维护的 GitHub Actions 目录或科学软件目录中。
  遵循各目录的贡献说明。
- 邀请早期用户介绍他们的使用场景，并在征得许可后添加一份简短的采用项目清单。
  宣布重大版本发布时，提供一个展示改进效果的具体示例。

## 添加实用的 README 徽章

ThreadScale 已有 Marketplace、测试状态和许可证徽章。星标徽章可以提供一个公开的关注度指标。
将以下 Markdown 复制到 action 的 README 中，并按需替换仓库名和工作流名：

```markdown
[![Marketplace][market-badge]][market]
[![Stars][stars-badge]][repo]
[![Tests][tests-badge]][tests]

[market-badge]: https://img.shields.io/badge/Marketplace-ThreadScale-2088FF
[stars-badge]: https://img.shields.io/github/stars/gemc/ThreadScale?style=flat
[tests-badge]: https://img.shields.io/github/actions/workflow/status/gemc/ThreadScale/test.yml
[market]: https://github.com/marketplace/actions/threadscale
[repo]: https://github.com/gemc/ThreadScale
[tests]: https://github.com/gemc/ThreadScale/actions/workflows/test.yml
```

[星标徽章][stars-docs] 统计星标数量；[工作流徽章][tests-docs] 显示 action 仓库的
测试状态。两者都无法衡量其他项目运行该 action 的频率。Marketplace 徽章是一个静态链接。
发布资产的下载量和仓库克隆量也不应被当作 action 的执行次数。

## 展示采用情况的证据

要提供有用的使用量徽章，请持续统计**已知使用该 action 的公开仓库数量**，并将徽章链接到
相应的证据。先从人工审核的清单开始；只有当维护变得繁琐时，再将更新自动化。
使用 [GitHub 代码搜索][search-docs] 查找可能的调用方：

```text
"gemc/ThreadScale@" path:.github/workflows/ NOT repo:gemc/ThreadScale
"gemc/ThreadScale/.github/workflows/thread-scaling.yml@" path:.github/workflows/ NOT repo:gemc/ThreadScale
```

检查匹配项中是否有仍在使用的 `uses:` 引用，对两次搜索结果中的仓库进行去重，并排除
不代表独立采用的派生仓库和复制的示例。记录日期和计数方法。
这只是部分计数：私有仓库、未被索引的调用方和间接调用方都会被遗漏，而且
工作流中的引用并不能证明它实际运行过。

要展示经过审核的计数，请在你的网站上发布一个小型 JSON 文件，并使用
[Shields 端点徽章][endpoint-docs]。例如，以下 JSON 使用 **N 作为占位符**；
请在发布前将其替换为核实后的计数：

```json
{
  "schemaVersion": 1,
  "label": "known public users",
  "message": "N repositories",
  "color": "blue"
}
```

然后使用以下 README 模板，将两个示例 URL 分别替换为你的 JSON 端点和证据页面：

```markdown
[![Known public users][usage-badge]][usage-evidence]

[usage-badge]: https://img.shields.io/endpoint?url=https%3A%2F%2Fexample.org%2Fusage.json
[usage-evidence]: https://example.org/adopters
```

要了解推广效果，仓库维护者还可以通过 **Insights → Traffic** 查看访客、
克隆量和引荐来源网站。GitHub 的[流量视图][traffic-docs] 提供过去 14 天的访客和
完整克隆数据；这些数据衡量的是仓库流量，而非 action 的运行次数。

[tags]: /home/mynotes/git#publish-an-immutable-release-and-move-its-major-version-tag
[publishing]:
  https://docs.github.com/en/actions/how-tos/create-and-publish-actions/publish-in-github-marketplace
[stars-docs]: https://shields.io/badges/git-hub-repo-stars
[tests-docs]: https://shields.io/badges/git-hub-actions-workflow-status
[endpoint-docs]: https://shields.io/badges/endpoint-badge
[search-docs]:
  https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[traffic-docs]:
  https://docs.github.com/articles/viewing-traffic-to-a-repository
