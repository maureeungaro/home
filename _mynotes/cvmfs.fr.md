---
layout: default
title: "CVMFS on macOS"
permalink: /mynotes/cvmfs.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# CVMFS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>
<br/>


Pour utiliser les points de montage **CernVM File System** sur un Mac, deux paquets sont nécessaires :

- [macFuse](https://macfuse.github.io)
- [CernVM-FS](https://cernvm.cern.ch/fs/)

<br/>

> [!IMPORTANT] Autorisations MacFuse
> Pendant l'installation, une invite devrait apparaître pour autoriser l'extension `Ben Fisher`. <br/>
> Cela peut aussi être vérifié avec la commande : <br/>
> ```shell
>    sudo kmutil load -p /Library/Filesystems/macfuse.fs/Contents/Extensions/26/macfuse.kext
> ```
> (remplacez 26 par la version de l'OS)<br/><br/>
> Si leur chargement n'est pas approuvé, allez dans `Settings > Privacy and Security > Security`, autorisez puis redémarrez.
