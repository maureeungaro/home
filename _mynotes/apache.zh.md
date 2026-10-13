---
layout: default
title: "Apache PHP server"
permalink: /mynotes/apache.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# 在本地模拟 Apache + PHP 服务器
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Docker Compose 可以在本地启动一个 Apache + PHP 服务器，而无需在主机上安装任何东西。
这对于在部署前开发和测试 PHP 页面非常有用。

<br/>

## docker-compose.yml

将此文件放在你想要提供服务的目录中：

```yaml
services:
  web:
    image: php:8.3-apache
    ports:
      - "8080:80"
    volumes:
      - .:/var/www/html
```

卷挂载 `.:/var/www/html` 将当前目录映射到 Apache 的文档根目录，
因此该目录中的每个文件都可以立即使用，无需重新构建。

若要改为提供某个子目录（例如 `web_portal/`）的服务，请将卷修改为：

```yaml
      - ./web_portal:/var/www/html
```

<br/>

## 启动与停止

在包含 `docker-compose.yml` 的目录中执行：

```shell
docker compose up -d
```

停止并删除容器：

```shell
docker compose down
```

<br/>

## 访问服务器

打开浏览器并访问：

```
http://localhost:8080/<filename>.php
```

例如，如果 `docker-compose.yml` 挂载了 `./web_portal`，并且该目录中包含 `type1.php`：

```
http://localhost:8080/type1.php
```

<br/>

## 实用命令

在页面加载时实时查看 Apache 的错误日志：

```shell
docker compose logs -f
```

在容器内打开一个 shell：

```shell
docker compose exec web bash
```

<br/>
<br/>
<br/>
<br/>
