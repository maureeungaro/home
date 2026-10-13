---
layout: default
title: "Apache PHP server"
permalink: /mynotes/apache.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Apache + PHP サーバーをローカルでエミュレートする
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Docker Compose を使えば、ホスト側に何もインストールすることなく、ローカルに Apache + PHP サーバーを起動できます。
これは PHP ページをデプロイする前に開発・テストするのに便利です。

<br/>

## docker-compose.yml

配信したいディレクトリに、このファイルを配置します。

```yaml
services:
  web:
    image: php:8.3-apache
    ports:
      - "8080:80"
    volumes:
      - .:/var/www/html
```

ボリュームマウント `.:/var/www/html` はカレントディレクトリを Apache のドキュメントルートにマッピングするため、
そのディレクトリ内のすべてのファイルが、再ビルドなしで即座に利用可能になります。

サブディレクトリ（例: `web_portal/`）を配信したい場合は、ボリュームを次のように変更します。

```yaml
      - ./web_portal:/var/www/html
```

<br/>

## 起動と停止

`docker-compose.yml` のあるディレクトリから実行します。

```shell
docker compose up -d
```

コンテナを停止して削除します。

```shell
docker compose down
```

<br/>

## サーバーへのアクセス

ブラウザを開いて、次の URL にアクセスします。

```
http://localhost:8080/<filename>.php
```

たとえば、`docker-compose.yml` が `./web_portal` をマウントしていて、そのディレクトリに `type1.php` が含まれている場合は次のようになります。

```
http://localhost:8080/type1.php
```

<br/>

## 便利なコマンド

ページの読み込み中に Apache のエラーログを追跡します。

```shell
docker compose logs -f
```

コンテナ内でシェルを開きます。

```shell
docker compose exec web bash
```

<br/>
<br/>
<br/>
<br/>
