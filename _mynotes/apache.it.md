---
layout: default
title: "Apache PHP server"
permalink: /mynotes/apache.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Emulare un server Apache + PHP in locale
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Docker Compose può avviare un server Apache + PHP locale senza installare nulla sull'host.
Questo è utile per sviluppare e testare pagine PHP prima di distribuirle.

<br/>

## docker-compose.yml

Colloca questo file nella directory che vuoi servire:

```yaml
services:
  web:
    image: php:8.3-apache
    ports:
      - "8080:80"
    volumes:
      - .:/var/www/html
```

Il montaggio del volume `.:/var/www/html` mappa la directory corrente sulla document root di Apache,
così ogni file in quella directory è immediatamente disponibile senza dover ricostruire nulla.

Per servire una sottodirectory (ad esempio `web_portal/`), modifica invece il volume in:

```yaml
      - ./web_portal:/var/www/html
```

<br/>

## Avvio e arresto

Dalla directory che contiene `docker-compose.yml`:

```shell
docker compose up -d
```

Arresta e rimuovi il container:

```shell
docker compose down
```

<br/>

## Accesso al server

Apri un browser e vai all'indirizzo:

```
http://localhost:8080/<filename>.php
```

Ad esempio, se `docker-compose.yml` monta `./web_portal` e quella directory contiene `type1.php`:

```
http://localhost:8080/type1.php
```

<br/>

## Comandi utili

Segui in tempo reale il log degli errori di Apache mentre una pagina viene caricata:

```shell
docker compose logs -f
```

Apri una shell all'interno del container:

```shell
docker compose exec web bash
```

<br/>
<br/>
<br/>
<br/>
