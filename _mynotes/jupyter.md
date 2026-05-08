---
layout: default
title: "Using Jupyter"
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Using Jupyter
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## mybinder

A public repository with a `Dockerfile` can be loaded into [binder](https://mybinder.org).
This allows running `jupyter` commands in it.

A typical layout of the repo:

```
binder-tutorials/
├── Dockerfile                  ← the Binder environment
├── notebooks/
│   ├── 00_demo1.ipynb
│   ├── 01_demo2.ipynb
│   └── 02_demo3.ipynb
└── README.md                   ← contains the launch badge
```


When first requested, the image is build in mybinder - but then it is cached for subsequent uses.