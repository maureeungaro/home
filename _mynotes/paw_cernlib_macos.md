---
layout: default
title: "Cernlib on MacOS"
---

{% include mynotes.html %}

# Cernlib, Paw on MacOS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Here is a quick way to run cernlib’s paw in a Docker container on MacOS[^1]. 
This uses a debian based container with paw, paw++, and cernlib installed via the system (i.e. apt-get).

[^1]: Credits to [David Lawrence Original Blog Post](https://davidljlab.wordpress.com/2018/10/03/cernlib-paw-docker/)

## Requirements

Install the Docker and X11 (XQuartz) apps:

- [Docker](https://www.docker.com)
- [XQuartz](https://www.xquartz.org)

After installing XQuartz, make sure to enable "Allow connections from network clients" in the Preferences > Security tab.
It should look like this:

{% include figure.html
   src="assets/images/notes/xquartz.png"
   alt="xquarts security preferences"
   caption="<br/>
   Allow connections from network clients. You may need to 
   restart XQuartz for the change to take effect."
   width="800"
%}

Run the following command in a terminal to allow X11 connections from Docker containers:

```bash
xhost +
```

## Running Paw/Cernlib in Docker

In the following instructions we assume you are using a Mac
with a silicon CPU (M1/M2/M3, etc). 
If you have an Intel CPU, remove the `--platform linux/amd64` option from the `docker run` command below.


In a terminal, run the following commands to create a script `dsh` that will launch an interactive
shell in the container:

```bash
docker pull jeffersonlab/cernlib:2004
docker run --rm -it --platform linux/amd64 jeffersonlab/cernlib:2004 cat /container/image/dsh | tr -d "\r" > dsh
chmod +x dsh
```

You're now ready to run Paw/Cernlib in Docker.
In a terminal, run the following command to launch an interactive shell in the container, and then start `paw++`:

```bash
./dsh jeffersonlab/cernlib:2004
paw++
```



<br/><br/>

<hr>

<br/><br/>
