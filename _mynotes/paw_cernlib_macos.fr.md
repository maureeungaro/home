---
layout: default
title: "Cernlib on macOS"
permalink: /mynotes/paw_cernlib_macos.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# Cernlib, Paw sur macOS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Voici une méthode rapide pour exécuter Paw de Cernlib dans un conteneur Docker sous macOS[^1].
Elle utilise un conteneur basé sur Debian avec paw, paw++ et Cernlib installés via le système (c'est-à-dire apt-get).

[^1]: Remerciements à David Lawrence pour son [article de blog original](https://davidljlab.wordpress.com/2018/10/03/cernlib-paw-docker/)

## Prérequis

Installez les applications Docker et X11 (XQuartz) :

- [Docker](https://www.docker.com)
- [XQuartz](https://www.xquartz.org)

Après avoir installé XQuartz, activez « Allow connections from network clients » dans Preferences > Security.
Cela devrait ressembler à ceci :

{% include figure.html
   src="/assets/images/notes/xquartz.png"
   alt="xquartz security preferences"
   caption="<br/>
   Allow connections from network clients. You may need to 
   restart XQuartz for the change to take effect."
   width="800"
%}

Exécutez la commande suivante dans un terminal pour autoriser les connexions X11 depuis les conteneurs Docker :

```shell
xhost +
```

## Exécuter Paw/Cernlib dans Docker

Dans les instructions qui suivent, nous supposons que vous utilisez un Mac
équipé d'un processeur Apple Silicon (M1/M2/M3, etc.).
Si vous avez un processeur Intel, retirez l'option `--platform linux/amd64` de la commande `docker run` ci-dessous.


Dans un terminal, exécutez les commandes suivantes pour créer un script `dsh` qui lancera un
shell interactif dans le conteneur :

```shell
docker pull jeffersonlab/cernlib:2004
docker run --rm -it --platform linux/amd64 jeffersonlab/cernlib:2004 cat /container/image/dsh | tr -d "\r" > dsh
chmod +x dsh
```

Vous êtes maintenant prêt à exécuter Paw/Cernlib dans Docker.
Dans un terminal, lancez un shell interactif dans le conteneur avec la commande suivante, puis démarrez `paw++` :

```shell
./dsh jeffersonlab/cernlib:2004
paw++
```



<br/><br/>

<hr>

<br/><br/>
