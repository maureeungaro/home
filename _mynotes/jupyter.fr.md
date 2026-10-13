---
layout: default
title: "Using Jupyter"
permalink: /mynotes/jupyter.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Utilisation de Jupyter
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## mybinder

Un dépôt public contenant un `Dockerfile` peut être chargé dans [binder](https://mybinder.org).
Cela permet d'y exécuter des commandes `jupyter`.

Une structure typique du dépôt :

```
binder-tutorials/
├── Dockerfile                  ← the Binder environment
├── notebooks/
│   ├── 00_demo1.ipynb
│   ├── 01_demo2.ipynb
│   └── 02_demo3.ipynb
└── README.md                   ← contains the launch badge
```


Lors de la première requête, l'image est construite sur mybinder, puis mise en cache pour les utilisations
suivantes.
