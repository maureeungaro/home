---
layout: default
title: "Docker and Apptainer"
---
{% include mynotes.html %}

# [Docker](https://www.docker.com)

To run a docker image using docker:

```bash
docker run -it --rm <image> command
```

where:

- `-it`: Lets you interact with the container as if it was a shell
- `--rm`: Automatically remove the container when it exits.
- `command`: a command to run within the container, typically `bash`

Mounting a local directory on the container for permanent storage can be achieved using the `-v` binding.
For example this will have the local `~/mywork` available on the container in `/usr/local/mywork`:

```bash
docker run -it --rm  -v ~/mywork:/usr/local/mywork <image> command
```

# Apptainer

Linux host have `apptainer` (formally singularity), that can be run similarly to docker. 
It uses a cache directory to store the images so I suggest to set that cache to 
a location with large disk capacity. In the following example `/path/to/user/cache` is used:

```bash
export sif_cache=/path/to/$USER/sif
```

and then:

```bash
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
