---
layout: default
title: "Using rsync"
---

{% include mynotes.html %}


# Using rsync
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

A typical usage of `rsync`:


```shell
rsync -av --progress /path/to/origin/ /path/to/destination/
```

where:

- `-a` = archive mode, preserves permissions, times, symlinks, etc.
- `-v` = verbose
- `origin` = copy the contents of origin
- `destination` = put them into destination
- `--progress` = show progress

<br/>

> [!IMPORTANT]
> This will create the exact tree structure of `origin` inside `destination`