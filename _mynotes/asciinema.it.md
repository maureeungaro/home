---
layout: default
title: "asciinema"
permalink: /mynotes/asciinema.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# Usare Asciinema e creare gif
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

- [Pagina principale di Asciinema](https://asciinema.org/)

## Registrare la digitazione

```
asciinema rec demo.cast
```
Premi `Ctrl + D` al termine della registrazione.


`asciinema upload demo.cast` restituirà l'indirizzo di una pagina che mostrerà come 
**incorporare** la registrazione in una pagina web o scaricarla come **gif**. 

È possibile aggiungere `data-autoplay="true" data-loop="true"` alla pagina.


<br/>

## Scripting

Lo script [asciinema-rec_script](https://raw.githubusercontent.com/maureeungaro/home/refs/heads/main/assets/asciinema-rec_script) può essere usato per registrare uno script.
                           
Ricorda di caricare l'ambiente necessario all'esecuzione dello script. 
Attualmente `asciinema-rec_script` non supporta la connessione tramite ssh a host remoti
e l'esecuzione di comandi su di essi.

```
asciinema-rec_script script_name.sh
```

<br/>



## [Agg]([agg](https://github.com/asciinema/agg)): da `.cast` a gif

Assicurati di:

- commentare tutti i comandi echo in /etc/zshrc_Apple_Terminal 
- ricordarti di impostare  `PROMPT_EOL_MARK=''` in .zshrc 

``` 
agg --theme asciinema --font-size 50 --cols 132 --rows 22 --speed 2  ifarm.cast ifarm.gif
```


> [!NOTE] 
> A novembre 2025 asciinema è alla v3, ma agg supporta solo la v2. Per convertire un file v3 in un file v2: <br/>
> `asciinema convert -f asciicast-v2 a.cast a-v2.cast`
 
<br/>
 

## [ffmpeg](https://www.ffmpeg.org): da `.mov` a gif

Ecco un esempio per convertire un file mov in una gif. I due passaggi garantiscono colori ottimali:

```shell
ffmpeg -i input.mov -vf "fps=15,scale=800:-1:flags=lanczos,palettegen" -y palette.png
ffmpeg -i input.mov -i palette.png -lavfi "fps=15,scale=800:-1:flags=lanczos[x];[x][1:v]paletteuse" -loop 0 output.gif
```

dove:

- `fps=15` → frequenza dei fotogrammi (riducila per ottenere un file più piccolo)
- `scale=800`:-1 → larghezza di 800 px, mantiene le proporzioni
- `flags=lanczos` → filtro di ridimensionamento ad alta qualità
- `-loop 0` → ciclo infinito

<br/>

## Altri trucchi per le gif

Per concatenare 3 gif:

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

dove:

- `-loop 0` – indica al codificatore GIF di ripetere l'animazione all'infinito (0 = infinito).
- `[0:v], [1:v], [2:v]` – prelevano il flusso video dall'ingresso #0 (a.gif).
- `FPS=15` – ricampiona a 15 fotogrammi al secondo



<br/>

Per assicurarti che una gif venga ripetuta all'infinito:

```shell
ffmpeg -i in.gif \
  -filter_complex "fps=15,split[x][z];[x]palettegen[p];[z][p]paletteuse" \
  -loop 0 out.gif
```

<br/>
