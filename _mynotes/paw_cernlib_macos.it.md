---
layout: default
title: "Cernlib on macOS"
permalink: /mynotes/paw_cernlib_macos.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# Cernlib, Paw su macOS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Ecco un modo rapido per eseguire Paw di Cernlib in un container Docker su macOS[^1]. 
Si utilizza un container basato su Debian con paw, paw++ e Cernlib installati tramite il sistema (ossia apt-get).

[^1]: Ringraziamenti a [David Lawrence per il post originale sul suo blog](https://davidljlab.wordpress.com/2018/10/03/cernlib-paw-docker/)

## Requisiti

Installa le applicazioni Docker e X11 (XQuartz):

- [Docker](https://www.docker.com)
- [XQuartz](https://www.xquartz.org)

Dopo aver installato XQuartz, abilita "Allow connections from network clients" nella scheda Preferences > Security.
Dovrebbe apparire così:

{% include figure.html
   src="assets/images/notes/xquartz.png"
   alt="xquartz security preferences"
   caption="<br/>
   Allow connections from network clients. You may need to 
   restart XQuartz for the change to take effect."
   width="800"
%}

Esegui il seguente comando in un terminale per consentire le connessioni X11 dai container Docker:

```shell
xhost +
```

## Esecuzione di Paw/Cernlib in Docker

Nelle istruzioni seguenti si presume che tu stia usando un Mac
con una CPU Apple Silicon (M1/M2/M3, ecc.). 
Se hai una CPU Intel, rimuovi l'opzione `--platform linux/amd64` dal comando `docker run` qui sotto.


In un terminale, esegui i seguenti comandi per creare uno script `dsh` che avvierà una
shell interattiva nel container:

```shell
docker pull jeffersonlab/cernlib:2004
docker run --rm -it --platform linux/amd64 jeffersonlab/cernlib:2004 cat /container/image/dsh | tr -d "\r" > dsh
chmod +x dsh
```

Ora sei pronto per eseguire Paw/Cernlib in Docker.
In un terminale, esegui il seguente comando per avviare una shell interattiva nel container, quindi avvia `paw++`:

```shell
./dsh jeffersonlab/cernlib:2004
paw++
```



<br/><br/>

<hr>

<br/><br/>
