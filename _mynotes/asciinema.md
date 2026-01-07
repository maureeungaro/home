---
layout: default
title: "asciinema"
---
{% include mynotes.html %}

# [Asciinema, gifs](https://asciinema.org/)
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

## Recording typing

```
asciinema rec demo.cast
```
Press `Ctrl + D` when done recording.


`asciinema upload demo.cast` will return the address - that will show how 
to **embed** it on a webpage or download a **gif**. 

Can add `data-autoplay="true" data-loop="true"` to the page.


<br/>

## Scripting

The [asciinema-rec_script](https://raw.githubusercontent.com/gemc/home/refs/heads/main/assets/asciinema-rec_script) script can be used to record a script.

Remember to load the environment needed by the running script. 
Currently `asciinema-rec_script` does not support ssh-ing into remote hosts
and running commands there.

```
asciinema-rec_script script_name.sh
```

<br/>



## [Agg]([agg](https://github.com/asciinema/agg)): from `.cast` to gif

Make sure to:

- comment out all echo commands in /etc/zshrc_Apple_Terminal 
- remember to set  `PROMPT_EOL_MARK=''` in .zshrc 

``` 
agg --theme asciinema --font-size 50 --cols 132 --rows 22 --speed 2  ifarm.cast ifarm.gif
```


> [!NOTE] 
> As of November 2025 asciinema is v3 but agg only supports v2. To convert a v3 to a v2: <br/>
> `asciinema convert -f asciicast-v2 a.cast a-v2.cast`
 
<br/>
 

## [ffmpeg](https://www.ffmpeg.org): from `.mov` gif

Here's an example to convert a mov file to a gif. The two steps ensure optimal colors:

```bash
ffmpeg -i input.mov -vf "fps=15,scale=800:-1:flags=lanczos,palettegen" -y palette.png
ffmpeg -i input.mov -i palette.png -lavfi "fps=15,scale=800:-1:flags=lanczos[x];[x][1:v]paletteuse" -loop 0 output.gif
```

where:

- `fps=15` → frame rate (lower for smaller file)
- `scale=800`:-1 → width 800 px, keep aspect ratio
- `flags=lanczos` → high-quality scaling filter
- `-loop 0` → infinite loop

<br/>

## Additional gif goodies

To concatenate 3 gifs:

```bash

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

where:

- `-loop 0` – tells the GIF encoder to loop forever (0 = infinite).
- `[0:v], [1:v], [2:v]` – take video stream from input #0 (a.gif).
- `FPS=15` – re-sample to 15 frames per second



<br/>

To make sure a gif loops forever:

```bash
ffmpeg -i in.gif \
  -filter_complex "fps=15,split[x][z];[x]palettegen[p];[z][p]paletteuse" \
  -loop 0 out.gif
```

<br/>


