---
layout: default
title: "CVMFS on macOS"
permalink: /mynotes/cvmfs.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# CVMFS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>
<br/>


要在 Mac 上使用 **CernVM File System** 挂载点，需要两个软件包：

- [macFuse](https://macfuse.github.io)
- [CernVM-FS](https://cernvm.cern.ch/fs/)

<br/>

> [!IMPORTANT] MacFuse 权限
> 安装过程中应会弹出提示，要求允许加载 `Ben Fisher` 扩展。 <br/>
> 也可以用以下命令进行检查： <br/>
> ```shell
>    sudo kmutil load -p /Library/Filesystems/macfuse.fs/Contents/Extensions/26/macfuse.kext
> ```
> （请将 26 替换为相应的操作系统版本号）<br/><br/>
> 如果扩展未获准加载，请前往 `Settings > Privacy and Security > Security`，允许加载后重启。
