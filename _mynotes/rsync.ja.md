---
layout: default
title: "Using rsync"
permalink: /mynotes/rsync.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# rsync の使い方
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

`rsync` の典型的な使い方は次のとおりです。


```shell
rsync -av --progress /path/to/origin/ /path/to/destination/
```

ここで、各項目の意味は以下のとおりです。

- `-a` = アーカイブモード。パーミッション、タイムスタンプ、シンボリックリンクなどを保持します
- `-v` = 詳細表示
- `origin` = コピー元の内容をコピーします
- `destination` = コピー先に配置します
- `--progress` = 進捗状況を表示します

<br/>

> [!IMPORTANT]
> これにより、`origin` のツリー構造がそのまま `destination` の中に作成されます
