---
layout: default
title: Docker, Apptainer
permalink: /mynotes/docker.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Docker et Apptainer
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Pour exécuter une image Docker avec Docker :

```shell
docker run -it --rm <image> command
```

où :

- `-it` : permet d'interagir avec le conteneur comme s'il s'agissait d'un shell
- `--rm` : supprime automatiquement le conteneur lorsqu'il se termine.
- `command` : une commande à exécuter dans le conteneur, généralement `bash`

Pour monter un répertoire local dans le conteneur afin de conserver les données, utilisez l'option `-v`.
Par exemple, le répertoire local `~/mywork` sera accessible dans le conteneur sous `/usr/local/mywork` :

```shell
docker run -it --rm  -v ~/mywork:/usr/local/mywork <image> command
```

<br/>

## Commandes utiles

Le mot-clé `CMD` du Dockerfile peut désigner un script qui sera exécuté si la
commande Docker `run` n'est pas incluse.

Le mot-clé `ENTRYPOINT` définit un script qui sera toujours exécuté dans le conteneur,
que l'option `command` soit incluse ou non.

Le point d'entrée peut être remplacé à l'exécution avec l'option ci-dessous (en prenant `sh` comme exemple) :

```shell
--entrypoint /bin/sh
```
<br/>

### Pour inspecter une image :

```shell
docker image inspect <image> 
```

<br/><br/>

## Apptainer

Les hôtes Linux disposent d'`apptainer` (anciennement Singularity), qui s'utilise de manière similaire à Docker.
Il utilise un répertoire de cache pour stocker les images ; je suggère donc de placer ce cache
sur un disque de grande capacité. Dans l'exemple suivant, `/path/to/user/cache` est utilisé :

```shell
export sif_cache=/path/to/$USER/sif
```

puis :

```shell
export APPTAINER_CACHEDIR=$sif_cache/apptainer-cache 
export APPTAINER_TMPDIR=$sif_cache/apptainer-tmp 
export TMPDIR=$sif_cache/apptainer-tmp 

apptainer exec --cleanenv --bind ~/mywork:/usr/local/mywork \
  <image> command
```



<br/>
<br/>
<br/>
<br/>
