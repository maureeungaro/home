---
layout: default
title: "Using Jupyter"
permalink: /mynotes/jupyter.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Jupyter の使用
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## mybinder

`Dockerfile` を含む公開リポジトリは [binder](https://mybinder.org) に読み込むことができます。
これにより、その環境で `jupyter` コマンドを実行できます。

リポジトリの典型的な構成は次のとおりです。

```
binder-tutorials/
├── Dockerfile                  ← the Binder environment
├── notebooks/
│   ├── 00_demo1.ipynb
│   ├── 01_demo2.ipynb
│   └── 02_demo3.ipynb
└── README.md                   ← contains the launch badge
```


最初のリクエスト時に、イメージは mybinder でビルドされ、その後の利用に備えてキャッシュされます。
