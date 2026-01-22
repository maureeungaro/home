---
layout: default
title: "Docker and Apptainer"
---
{% include mynotes.html %}

# Docker and Apptainer
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

To run a docker image using docker:

```shell
docker run -it --rm <image> command
```

where:

- `-it`: Lets you interact with the container as if it was a shell
- `--rm`: Automatically remove the container when it exits.
- `command`: a command to run within the container, typically `bash`

Mounting a local directory on the container for permanent storage can be achieved using the `-v` binding.
For example this will have the local `~/mywork` available on the container in `/usr/local/mywork`:

```shell
docker run -it --rm  -v ~/mywork:/usr/local/mywork <image> command
```

<br/>

## Useful commands

The dockerfile keyworkd `CMD` can point to a script that will run if the 
docker run `command` flag is not included. 

The keyworkd `ENTRYPOINT` defines a script that will always run in the container, regardless
if the  `command` flag is included or not.

The entrypoint can be overwrittten at run time with the option (using `sh` as an example here):

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

Linux host have `apptainer` (formally singularity), that can be run similarly to docker. 
It uses a cache directory to store the images so I suggest to set that cache to 
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
