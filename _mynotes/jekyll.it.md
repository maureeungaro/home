---
layout: default
title: "Using Jekyll"
permalink: /mynotes/jekyll.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Usare Jekyll
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

- [Pagina principale di Jekyll](https://jekyllrb.com)

## Comandi vari: 

Per avviare un server Jekyll, ripulire i file generati, aggiornare Jekyll e installare i bundle, esegui:

```shell
bundle exec jekyll serve
bundle exec jekyll clean 
bundle update jekyll
bundle install
```

- Se il gemfile viene modificato, è necessario eseguire `bundle`
- Se il file YAML di configurazione viene modificato (per esempio aggiornando il tema), è necessario eseguire `bundle update`

<br/>

> [!CAUTION]
> A volte `Gemfile.lock` vincola l'uso a una versione diversa di Bundler. Verifica:
> 
> ```bash
> gem list bundler
> tail -n +1 Gemfile.lock | sed -n '/BUNDLED WITH/,$p'
> ```
> Rimuovere il file risolve il problema.

> [!IMPORTANT] 
> non eseguire mai e poi mai bundle con `sudo`

<br/>

Per aggiornare Bundler a una versione compatibile con la tua versione di Ruby e verificare / disinstallare le vecchie versioni:

```shell
sudo gem update --system
sudo gem update bundler
sudo gem install bundler 
gem list bundler    
sudo gem uninstall bundler -v 2.6.5
```

A volte è necessario rimuovere completamente Bundler e reinstallarlo:

```shell
sudo rm -f /opt/homebrew/bin/bundle /opt/homebrew/bin/bundler
sudo gem uninstall bundler -aIx
```

<br/>


## Estensioni mancanti

I seguenti messaggi:

```html
Source locally installed gems is ignoring #<Bundler::StubSpecification name=nokogiri version=1.18.3 platform=ruby> because it is missing extensions
```

Possono essere risolti eseguendo:

```shell
gem pristine <module>
bundle install
```

<br/>

## Stile

- Si usa [Minima](https://github.com/jekyll/minima#readme)
- L'ordine delle schede è determinato dal nome del file, quindi puoi anteporre `a_` ecc.
- Elenco dei font: https://fonts.google.com
- La posizione dei file di Minima può essere individuata con `bundle show minima`. 



<br/>

## Avvisi:

Aggiungere quanto segue al gruppo `jekyll_plugins` nel `gemfile` abilita gli avvisi nei file Markdown:

```
  gem "jekyll-gfm-admonitions"
```

Gli avvisi possono essere creati così:

```markdown
> [!NOTE] 
> Note text line1
> Note text line2
```

Gli avvisi disponibili sono:


```markdown
[!NOTE], [!TIP], [!WARNING], [!CAUTION], [!IMPORTANT]
```

<br/>




## Aggiungere contenuti

I file nelle directory il cui nome inizia con un trattino basso
non vengono elaborati da Jekyll se specificati nel file _config.yml in questo modo:

```markdown
# this add content to the website from the local dirs starting with _
collections:
  pi0:
    output: true
```

<br/>

Facoltativamente è possibile aggiungere i [permalink](https://jekyllrb.com/docs/permalinks/) per la navigazione.


<br/>

## Funzionalità aggiuntive di Markdown

- Link web: 
```
This site was built using [GitHub Pages](https://pages.github.com/).
```

- Link alle sezioni:
```
See the [Admonitions](#admonitions) section for more details.
```

- Indirizzi email:
```
You can contact me at [gemc@jlab.org](mailto:gemc@jlab.org)
```

<br/>




<br/>

## Link utili:

- [Jekyll su GitHub](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [Tutorial di Jekyll](https://jekyllrb.com/docs/step-by-step/01-setup/)
- [Tabelle accattivanti](https://github.com/jeffreytse/jekyll-spaceship)
