---
layout: default
title: "asciinema"
permalink: /mynotes/asciinema.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# 使用 Asciinema 并创建 gif
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

- [Asciinema 主页](https://asciinema.org/)

## 录制键入过程

```
asciinema rec demo.cast
```
录制完成后按 `Ctrl + D`。


`asciinema upload demo.cast` 会返回一个地址——访问该地址即可了解如何将录制内容
**嵌入**到网页中，或下载为 **gif**。

可以在页面中加入 `data-autoplay="true" data-loop="true"`。


<br/>

## 脚本化录制

可以使用 [asciinema-rec_script](https://raw.githubusercontent.com/maureeungaro/home/refs/heads/main/assets/asciinema-rec_script) 脚本来录制脚本的执行过程。
                           
请记得先加载运行脚本所需的环境。
目前 `asciinema-rec_script` 不支持通过 ssh 登录到远程主机
并在其上运行命令。

```
asciinema-rec_script script_name.sh
```

<br/>



## [Agg]([agg](https://github.com/asciinema/agg))：从 `.cast` 到 gif

请确保：

- 注释掉 /etc/zshrc_Apple_Terminal 中的所有 echo 命令
- 记得在 .zshrc 中设置  `PROMPT_EOL_MARK=''`

``` 
agg --theme asciinema --font-size 50 --cols 132 --rows 22 --speed 2  ifarm.cast ifarm.gif
```


> [!NOTE] 
> 截至 2025 年 11 月，asciinema 已是 v3，但 agg 仅支持 v2。将 v3 转换为 v2 的方法：<br/>
> `asciinema convert -f asciicast-v2 a.cast a-v2.cast`
 
<br/>
 

## [ffmpeg](https://www.ffmpeg.org)：从 `.mov` 到 gif

下面是一个将 mov 文件转换为 gif 的示例。这两个步骤可确保获得最佳色彩：

```shell
ffmpeg -i input.mov -vf "fps=15,scale=800:-1:flags=lanczos,palettegen" -y palette.png
ffmpeg -i input.mov -i palette.png -lavfi "fps=15,scale=800:-1:flags=lanczos[x];[x][1:v]paletteuse" -loop 0 output.gif
```

其中：

- `fps=15` → 帧率（越低，文件越小）
- `scale=800`:-1 → 宽度 800 像素，保持宽高比
- `flags=lanczos` → 高质量缩放滤镜
- `-loop 0` → 无限循环

<br/>

## 更多 gif 小技巧

拼接 3 个 gif：

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

其中：

- `-loop 0` – 让 GIF 编码器无限循环（0 = 无限）。
- `[0:v], [1:v], [2:v]` – 从输入 #0（a.gif）获取视频流。
- `FPS=15` – 重采样为每秒 15 帧



<br/>

确保 gif 无限循环：

```shell
ffmpeg -i in.gif \
  -filter_complex "fps=15,split[x][z];[x]palettegen[p];[z][p]paletteuse" \
  -loop 0 out.gif
```

<br/>
