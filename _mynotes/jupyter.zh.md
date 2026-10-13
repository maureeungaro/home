---
layout: default
title: "Using Jupyter"
permalink: /mynotes/jupyter.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# 使用 Jupyter
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## mybinder

包含 `Dockerfile` 的公共仓库可以加载到 [binder](https://mybinder.org) 中。
这样就可以在其中运行 `jupyter` 命令。

仓库的典型布局如下：

```
binder-tutorials/
├── Dockerfile                  ← the Binder environment
├── notebooks/
│   ├── 00_demo1.ipynb
│   ├── 01_demo2.ipynb
│   └── 02_demo3.ipynb
└── README.md                   ← contains the launch badge
```


首次请求时，镜像会在 mybinder 中构建——此后便会被缓存，供后续使用。
