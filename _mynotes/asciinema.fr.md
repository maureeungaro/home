---
layout: default
title: "asciinema"
permalink: /mynotes/asciinema.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# Utiliser Asciinema et créer des gifs
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

- [Accueil Asciinema](https://asciinema.org/)

## Enregistrer la saisie

```
asciinema rec demo.cast
```
Appuyez sur `Ctrl + D` lorsque l'enregistrement est terminé.


`asciinema upload demo.cast` renverra une adresse où vous trouverez comment
**intégrer** l'enregistrement à une page web ou le télécharger au format **gif**.

Vous pouvez ajouter `data-autoplay="true" data-loop="true"` à la page.


<br/>

## Utilisation de scripts

Le script [asciinema-rec_script](https://raw.githubusercontent.com/maureeungaro/home/refs/heads/main/assets/asciinema-rec_script) peut être utilisé pour enregistrer l'exécution d'un script.
                           
Pensez à charger l'environnement requis par le script exécuté.
Actuellement, `asciinema-rec_script` ne prend pas en charge la connexion SSH à des hôtes distants
ni l'exécution de commandes sur ceux-ci.

```
asciinema-rec_script script_name.sh
```

<br/>



## [Agg]([agg](https://github.com/asciinema/agg)) : de `.cast` au gif

Assurez-vous de :

- mettre en commentaire toutes les commandes echo dans /etc/zshrc_Apple_Terminal
- penser à définir  `PROMPT_EOL_MARK=''` dans .zshrc

``` 
agg --theme asciinema --font-size 50 --cols 132 --rows 22 --speed 2  ifarm.cast ifarm.gif
```


> [!NOTE] 
> En novembre 2025, asciinema est en v3 mais agg ne prend en charge que la v2. Pour convertir un enregistrement v3 en v2 : <br/>
> `asciinema convert -f asciicast-v2 a.cast a-v2.cast`
 
<br/>
 

## [ffmpeg](https://www.ffmpeg.org) : de `.mov` au gif

Voici un exemple pour convertir un fichier mov en gif. Les deux étapes garantissent des couleurs optimales :

```shell
ffmpeg -i input.mov -vf "fps=15,scale=800:-1:flags=lanczos,palettegen" -y palette.png
ffmpeg -i input.mov -i palette.png -lavfi "fps=15,scale=800:-1:flags=lanczos[x];[x][1:v]paletteuse" -loop 0 output.gif
```

où :

- `fps=15` → fréquence d'images (à réduire pour obtenir un fichier plus petit)
- `scale=800`:-1 → largeur de 800 px, conserve les proportions
- `flags=lanczos` → filtre de mise à l'échelle de haute qualité
- `-loop 0` → boucle infinie

<br/>

## Astuces supplémentaires pour les gifs

Pour concaténer 3 gifs :

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

où :

- `-loop 0` – indique à l'encodeur GIF de boucler indéfiniment (0 = infini).
- `[0:v], [1:v], [2:v]` – récupèrent le flux vidéo de l'entrée #0 (a.gif).
- `FPS=15` – rééchantillonne à 15 images par seconde



<br/>

Pour s'assurer qu'un gif boucle indéfiniment :

```shell
ffmpeg -i in.gif \
  -filter_complex "fps=15,split[x][z];[x]palettegen[p];[z][p]paletteuse" \
  -loop 0 out.gif
```

<br/>
