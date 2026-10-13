---
layout: default
title: "Using rsync"
permalink: /mynotes/rsync.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Uso di rsync
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Un utilizzo tipico di `rsync`:


```shell
rsync -av --progress /path/to/origin/ /path/to/destination/
```

dove:

- `-a` = modalità archivio, preserva permessi, timestamp, collegamenti simbolici, ecc.
- `-v` = output dettagliato
- `origin` = copia il contenuto dell'origine
- `destination` = inseriscilo nella destinazione
- `--progress` = mostra l'avanzamento

<br/>

> [!IMPORTANT]
> Questo creerà l'esatta struttura ad albero di `origin` all'interno di `destination`
