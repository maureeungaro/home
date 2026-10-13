---
layout: default
title: "Cernlib on macOS"
permalink: /mynotes/paw_cernlib_macos.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# macOS での Cernlib、Paw
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

macOS 上で Docker コンテナを使って Cernlib の Paw を手軽に動かす方法を紹介します[^1]。
この方法では、paw、paw++、および Cernlib がシステム経由（つまり apt-get）でインストールされた Debian ベースのコンテナを使用します。

[^1]: [David Lawrence 氏による元のブログ記事](https://davidljlab.wordpress.com/2018/10/03/cernlib-paw-docker/)に感謝します。

## 必要なもの

Docker と X11（XQuartz）アプリをインストールします。

- [Docker](https://www.docker.com)
- [XQuartz](https://www.xquartz.org)

XQuartz をインストールしたら、環境設定の「セキュリティ」タブで「ネットワーククライアントからの接続を許可」を必ず有効にしてください。
次のような表示になります。

{% include figure.html
   src="assets/images/notes/xquartz.png"
   alt="xquartz security preferences"
   caption="<br/>
   Allow connections from network clients. You may need to 
   restart XQuartz for the change to take effect."
   width="800"
%}

ターミナルで次のコマンドを実行し、Docker コンテナからの X11 接続を許可します。

```shell
xhost +
```

## Docker での Paw/Cernlib の実行

以下の手順では、Apple Silicon CPU（M1/M2/M3 など）を搭載した Mac を
使用していることを前提としています。
Intel CPU の場合は、以下の `docker run` コマンドから `--platform linux/amd64` オプションを削除してください。


ターミナルで次のコマンドを実行し、コンテナ内でインタラクティブシェルを起動する
スクリプト `dsh` を作成します。

```shell
docker pull jeffersonlab/cernlib:2004
docker run --rm -it --platform linux/amd64 jeffersonlab/cernlib:2004 cat /container/image/dsh | tr -d "\r" > dsh
chmod +x dsh
```

これで Docker 上で Paw/Cernlib を実行する準備が整いました。
ターミナルで次のコマンドを実行してコンテナ内でインタラクティブシェルを起動し、続いて `paw++` を起動します。

```shell
./dsh jeffersonlab/cernlib:2004
paw++
```



<br/><br/>

<hr>

<br/><br/>
