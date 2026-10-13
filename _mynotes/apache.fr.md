---
layout: default
title: "Apache PHP server"
permalink: /mynotes/apache.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Émuler un serveur Apache + PHP en local
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Docker Compose permet de démarrer un serveur Apache + PHP en local sans rien installer sur la machine hôte.
C'est pratique pour développer et tester des pages PHP avant de les déployer.

<br/>

## docker-compose.yml

Placez ce fichier dans le répertoire que vous souhaitez servir :

```yaml
services:
  web:
    image: php:8.3-apache
    ports:
      - "8080:80"
    volumes:
      - .:/var/www/html
```

Le montage de volume `.:/var/www/html` fait correspondre le répertoire courant à la racine documentaire
d'Apache, si bien que chaque fichier de ce répertoire est immédiatement disponible sans reconstruction.

Pour servir un sous-répertoire (par exemple `web_portal/`) à la place, modifiez le volume ainsi :

```yaml
      - ./web_portal:/var/www/html
```

<br/>

## Démarrer et arrêter

Depuis le répertoire contenant `docker-compose.yml` :

```shell
docker compose up -d
```

Arrêter et supprimer le conteneur :

```shell
docker compose down
```

<br/>

## Accéder au serveur

Ouvrez un navigateur et rendez-vous à l'adresse :

```
http://localhost:8080/<filename>.php
```

Par exemple, si `docker-compose.yml` monte `./web_portal` et que ce répertoire contient `type1.php` :

```
http://localhost:8080/type1.php
```

<br/>

## Commandes utiles

Suivre en continu le journal d'erreurs d'Apache pendant le chargement d'une page :

```shell
docker compose logs -f
```

Ouvrir un shell à l'intérieur du conteneur :

```shell
docker compose exec web bash
```

<br/>
<br/>
<br/>
<br/>
