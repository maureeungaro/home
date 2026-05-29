---
layout: default
title: "Apache PHP server"
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Emulating an Apache + PHP server locally
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Docker Compose can spin up a local Apache + PHP server without installing anything on the host.
This is useful for developing and testing PHP pages before deploying them.

<br/>

## docker-compose.yml

Place this file in the directory you want to serve:

```yaml
services:
  web:
    image: php:8.3-apache
    ports:
      - "8080:80"
    volumes:
      - .:/var/www/html
```

The volume mount `.:/var/www/html` maps the current directory to the Apache document root,
so every file in that directory is immediately available without rebuilding.

To serve a subdirectory (e.g. `web_portal/`) instead, change the volume to:

```yaml
      - ./web_portal:/var/www/html
```

<br/>

## Starting and stopping

From the directory containing `docker-compose.yml`:

```shell
docker compose up -d
```

Stop and remove the container:

```shell
docker compose down
```

<br/>

## Accessing the server

Open a browser and navigate to:

```
http://localhost:8080/<filename>.php
```

For example, if `docker-compose.yml` mounts `./web_portal` and that directory contains `type1.php`:

```
http://localhost:8080/type1.php
```

<br/>

## Useful commands

Tail the Apache error log while a page is loading:

```shell
docker compose logs -f
```

Open a shell inside the container:

```shell
docker compose exec web bash
```

<br/>
<br/>
<br/>
<br/>
