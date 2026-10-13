---
layout: default
title: "asciinema"
permalink: /mynotes/asciinema.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# Asciinema の利用と gif の作成
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

- [Asciinema ホーム](https://asciinema.org/)

## タイピングの録画

```
asciinema rec demo.cast
```
録画を終えるには `Ctrl + D` を押します。


`asciinema upload demo.cast` を実行するとアドレスが返されます。そこには Web ページへの
**埋め込み**方法や **gif** のダウンロード方法が表示されます。

ページには `data-autoplay="true" data-loop="true"` を追加できます。


<br/>

## スクリプトによる録画

[asciinema-rec_script](https://raw.githubusercontent.com/maureeungaro/home/refs/heads/main/assets/asciinema-rec_script) スクリプトを使うと、スクリプトの実行を録画できます。
                           
実行するスクリプトが必要とする環境を読み込むのを忘れないでください。
現時点では `asciinema-rec_script` はリモートホストへの ssh 接続や
そこでのコマンド実行には対応していません。

```
asciinema-rec_script script_name.sh
```

<br/>



## [Agg]([agg](https://github.com/asciinema/agg)): `.cast` から gif へ

必ず次を行ってください:

- /etc/zshrc_Apple_Terminal 内のすべての echo コマンドをコメントアウトする
- .zshrc で  `PROMPT_EOL_MARK=''` を設定するのを忘れない

``` 
agg --theme asciinema --font-size 50 --cols 132 --rows 22 --speed 2  ifarm.cast ifarm.gif
```


> [!NOTE] 
> 2025 年 11 月時点で asciinema は v3 ですが、agg は v2 にしか対応していません。v3 を v2 に変換するには: <br/>
> `asciinema convert -f asciicast-v2 a.cast a-v2.cast`
 
<br/>
 

## [ffmpeg](https://www.ffmpeg.org): `.mov` から gif へ

mov ファイルを gif に変換する例を以下に示します。2 段階に分けることで最適な色再現が得られます:

```shell
ffmpeg -i input.mov -vf "fps=15,scale=800:-1:flags=lanczos,palettegen" -y palette.png
ffmpeg -i input.mov -i palette.png -lavfi "fps=15,scale=800:-1:flags=lanczos[x];[x][1:v]paletteuse" -loop 0 output.gif
```

各項目の意味:

- `fps=15` → フレームレート（ファイルを小さくするには下げる）
- `scale=800`:-1 → 幅 800 px、アスペクト比を維持
- `flags=lanczos` → 高品質なスケーリングフィルタ
- `-loop 0` → 無限ループ

<br/>

## その他の gif 活用方法

3 つの gif を連結するには:

```shell

W=860
H=600
FPS=15

ffmpeg -i a.gif -i b.gif -i c.gif \
  -filter_complex "\
[0:v]fps=${FPS},scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2[v0]; \
[1:v]fps=${FPS},scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2[v1]; \
[2:v]fps=${FPS},scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2[v2]; \
[v0][v1][v2]concat=n=3:v=1:a=0,scale=${W}:${H},split[x][y]; \
[x]palettegen=reserve_transparent=1[p]; \
[y][p]paletteuse=dither=bayer" \
  -loop 0 out.gif

```

各項目の意味:

- `-loop 0` – GIF エンコーダに無限ループを指定する（0 = 無限）。
- `[0:v], [1:v], [2:v]` – 入力 #0（a.gif）から映像ストリームを取り出す。
- `FPS=15` – 毎秒 15 フレームに再サンプリングする



<br/>

gif を確実に無限ループさせるには:

```shell
ffmpeg -i in.gif \
  -filter_complex "fps=15,split[x][z];[x]palettegen[p];[z][p]paletteuse" \
  -loop 0 out.gif
```

<br/>
