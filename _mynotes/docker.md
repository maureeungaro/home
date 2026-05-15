---
layout: default
title: Docker, Apptainer
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Docker and Apptainer
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

To run a Docker image using Docker:

```shell
docker run -it --rm <image> command
```

where:

- `-it`: Lets you interact with the container as if it was a shell
- `--rm`: Automatically remove the container when it exits.
- `command`: a command to run within the container, typically `bash`

Mounting a local directory in the container for permanent storage can be achieved using the `-v` binding.
For example, this will make the local `~/mywork` available in the container as `/usr/local/mywork`:

```shell
docker run -it --rm  -v ~/mywork:/usr/local/mywork <image> command
```

<br/>

## Useful commands

The Dockerfile keyword `CMD` can point to a script that will run if the 
Docker `run` command is not included. 

The keyword `ENTRYPOINT` defines a script that will always run in the container, regardless
of whether the `command` flag is included.

The entrypoint can be overwritten at runtime with the option below (using `sh` as an example):

```shell
--entrypoint /bin/sh
```
<br/>

### To inspect an image:

```shell
docker image inspect <image> 
```

<br/><br/>

## Apptainer

Linux hosts have `apptainer` (formerly Singularity), which can be run similarly to Docker. 
It uses a cache directory to store the images, so I suggest setting that cache to 
a location with large disk capacity. In the following example `/path/to/user/cache` is used:

```shell
export sif_cache=/path/to/$USER/sif
```

and then:

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
