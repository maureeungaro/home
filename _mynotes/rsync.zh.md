---
layout: default
title: "Using rsync"
permalink: /mynotes/rsync.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# 使用 rsync
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

`rsync` 的典型用法：


```shell
rsync -av --progress /path/to/origin/ /path/to/destination/
```

其中：

- `-a` = 归档模式，保留权限、时间戳、符号链接等
- `-v` = 详细输出
- `origin` = 复制 origin 的内容
- `destination` = 将其放入 destination
- `--progress` = 显示进度

<br/>

> [!IMPORTANT]
> 这会在 `destination` 内部创建与 `origin` 完全相同的树状结构
