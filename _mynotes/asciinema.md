---
layout: default
title: "asciinema"
---
{% include mynotes.html %}

# [Asciinema](https://asciinema.org/)

---

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


## [Agg]([agg](https://github.com/asciinema/agg)) to create a gif

Make sure to:

- comment out all echo commands in /etc/zshrc_Apple_Terminal 
- remember to set  PROMPT_EOL_MARK='' in .zshrc 

``` 
agg --theme asciinema --font-size 50 --cols 112 --rows 22 --speed 2  ifarm.cast ifarm.gif
```

<br/>


## Scripting

The [asciinema-rec_script](https://raw.githubusercontent.com/gemc/home/refs/heads/main/assets/asciinema-rec_script.sh) script can be used to record a script.

Remember to load the environment .

```
./asciinema-rec_script script_name.sh
```