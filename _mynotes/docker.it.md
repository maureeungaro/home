---
layout: default
title: Docker, Apptainer
permalink: /mynotes/docker.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Docker e Apptainer
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Per eseguire un'immagine Docker tramite Docker:

```shell
docker run -it --rm <image> command
```

dove:

- `-it`: permette di interagire con il container come se fosse una shell
- `--rm`: rimuove automaticamente il container quando termina.
- `command`: un comando da eseguire all'interno del container, tipicamente `bash`

Per montare una directory locale nel container e archiviare i dati in modo permanente, si può usare il binding `-v`.
Ad esempio, questo renderà la directory locale `~/mywork` disponibile nel container come `/usr/local/mywork`:

```shell
docker run -it --rm  -v ~/mywork:/usr/local/mywork <image> command
```

<br/>

## Comandi utili

La parola chiave `CMD` del Dockerfile può indicare uno script che verrà eseguito se il
comando Docker `run` non viene incluso.

La parola chiave `ENTRYPOINT` definisce uno script che verrà sempre eseguito nel container, indipendentemente
dal fatto che il flag `command` sia incluso o meno.

L'entrypoint può essere sovrascritto a runtime con l'opzione seguente (usando `sh` come esempio):

```shell
--entrypoint /bin/sh
```
<br/>

### Per ispezionare un'immagine:

```shell
docker image inspect <image> 
```

<br/><br/>

## Apptainer

Gli host Linux dispongono di `apptainer` (in precedenza Singularity), che può essere eseguito come Docker.
Utilizza una directory di cache per memorizzare le immagini, quindi consiglio di collocare tale cache in
una posizione con molto spazio su disco. Nell'esempio seguente viene usato `/path/to/user/cache`:

```shell
export sif_cache=/path/to/$USER/sif
```

e poi:

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
