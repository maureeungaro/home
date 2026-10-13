---
layout: default
title: "Using Jupyter"
permalink: /mynotes/jupyter.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Usare Jupyter
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## mybinder

Un repository pubblico contenente un `Dockerfile` può essere caricato su [binder](https://mybinder.org).
Questo permette di eseguire comandi `jupyter` al suo interno.

Una tipica struttura del repository:

```
binder-tutorials/
├── Dockerfile                  ← the Binder environment
├── notebooks/
│   ├── 00_demo1.ipynb
│   ├── 01_demo2.ipynb
│   └── 02_demo3.ipynb
└── README.md                   ← contains the launch badge
```


Alla prima richiesta, l'immagine viene creata su mybinder e poi memorizzata nella cache per gli usi successivi.
