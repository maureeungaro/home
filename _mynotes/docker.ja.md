---
layout: default
title: Docker, Apptainer
permalink: /mynotes/docker.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Docker と Apptainer
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Docker を使って Docker イメージを実行するには:

```shell
docker run -it --rm <image> command
```

各項目の意味は次のとおりです:

- `-it`: コンテナをシェルのように対話的に操作できるようにします
- `--rm`: コンテナ終了時にコンテナを自動的に削除します。
- `command`: コンテナ内で実行するコマンドで、通常は `bash` です

永続的な保存のためにローカルディレクトリをコンテナにマウントするには、`-v` バインディングを使用します。
たとえば次のようにすると、ローカルの `~/mywork` がコンテナ内で `/usr/local/mywork` として利用できるようになります:

```shell
docker run -it --rm  -v ~/mywork:/usr/local/mywork <image> command
```

<br/>

## 便利なコマンド

Dockerfile のキーワード `CMD` は、Docker の `run` コマンドが指定されていない場合に実行される
スクリプトを指定できます。

キーワード `ENTRYPOINT` は、`command` フラグが含まれているかどうかに関係なく、コンテナ内で常に実行される
スクリプトを定義します。

エントリポイントは、実行時に次のオプションで上書きできます（ここでは `sh` を例として使用）:

```shell
--entrypoint /bin/sh
```
<br/>

### イメージを調べるには:

```shell
docker image inspect <image> 
```

<br/><br/>

## Apptainer

Linux ホストには `apptainer`（旧称 Singularity）があり、Docker と同様に実行できます。
イメージの保存にはキャッシュディレクトリを使用するため、そのキャッシュは
ディスク容量に余裕のある場所に設定することをお勧めします。以下の例では `/path/to/user/cache` を使用しています:

```shell
export sif_cache=/path/to/$USER/sif
```

続いて:

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
