---
layout: default
title: "CVMFS on macOS"
permalink: /mynotes/cvmfs.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# CVMFS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>
<br/>


Mac で **CernVM File System** のマウントポイントを使用するには、2 つのパッケージが必要です。

- [macFuse](https://macfuse.github.io)
- [CernVM-FS](https://cernvm.cern.ch/fs/)

<br/>

> [!IMPORTANT] MacFuse の権限
> インストール中に、`Ben Fisher` の拡張機能を許可するプロンプトが表示されるはずです。<br/>
> これは次のコマンドでも確認できます。<br/>
> ```shell
>    sudo kmutil load -p /Library/Filesystems/macfuse.fs/Contents/Extensions/26/macfuse.kext
> ```
> (26 はお使いの OS バージョンに置き換えてください)<br/><br/>
> ロードが承認されていない場合は、`Settings > Privacy and Security > Security` に移動し、許可してから再起動してください。
