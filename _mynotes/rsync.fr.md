---
layout: default
title: "Using rsync"
permalink: /mynotes/rsync.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Utilisation de rsync
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Une utilisation typique de `rsync` :


```shell
rsync -av --progress /path/to/origin/ /path/to/destination/
```

où :

- `-a` = mode archive, préserve les permissions, les horodatages, les liens symboliques, etc.
- `-v` = mode verbeux
- `origin` = copie le contenu de l'origine
- `destination` = place ce contenu dans la destination
- `--progress` = affiche la progression

<br/>

> [!IMPORTANT]
> Cela recréera exactement l'arborescence de `origin` à l'intérieur de `destination`
