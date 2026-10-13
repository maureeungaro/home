---
layout: default
title: "CVMFS on macOS"
permalink: /mynotes/cvmfs.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# CVMFS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>
<br/>


Per usare i punti di montaggio del **CernVM File System** su un Mac, sono necessari due pacchetti:

- [macFuse](https://macfuse.github.io)
- [CernVM-FS](https://cernvm.cern.ch/fs/)

<br/>

> [!IMPORTANT] Permessi di MacFuse
> Durante l'installazione dovrebbe comparire una richiesta per autorizzare l'estensione di `Ben Fisher`. <br/>
> Questo si può verificare anche con il comando: <br/>
> ```shell
>    sudo kmutil load -p /Library/Filesystems/macfuse.fs/Contents/Extensions/26/macfuse.kext
> ```
> (sostituire 26 con la versione del sistema operativo)<br/><br/>
> Se il caricamento non è autorizzato, andare in `Settings > Privacy and Security > Security`, autorizzarlo e riavviare.
