---
layout: default
title: "Using Jekyll"
permalink: /mynotes/jekyll.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Utilisation de Jekyll
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

- [Accueil de Jekyll](https://jekyllrb.com)

## Diverses commandes : 

Pour démarrer un serveur Jekyll, nettoyer, mettre à jour et installer les dépendances, exécutez :

```shell
bundle exec jekyll serve
bundle exec jekyll clean 
bundle update jekyll
bundle install
```

- Si le gemfile est modifié, il faut exécuter `bundle`
- Si le fichier YAML de configuration est modifié (par exemple pour changer de thème), il faut exécuter `bundle update`

<br/>

> [!CAUTION]
> Parfois, `Gemfile.lock` impose une version différente de Bundler. Vérifiez :
> 
> ```bash
> gem list bundler
> tail -n +1 Gemfile.lock | sed -n '/BUNDLED WITH/,$p'
> ```
> La suppression du fichier résout le problème.

> [!IMPORTANT] 
> N'exécutez jamais, au grand jamais, bundle avec `sudo`

<br/>

Pour mettre à jour Bundler vers une version compatible avec votre version de Ruby et vérifier / désinstaller les anciennes versions :

```shell
sudo gem update --system
sudo gem update bundler
sudo gem install bundler 
gem list bundler    
sudo gem uninstall bundler -v 2.6.5
```

Il faut parfois supprimer complètement Bundler et le réinstaller :

```shell
sudo rm -f /opt/homebrew/bin/bundle /opt/homebrew/bin/bundler
sudo gem uninstall bundler -aIx
```

<br/>


## Extensions manquantes

Les messages suivants :

```html
Source locally installed gems is ignoring #<Bundler::StubSpecification name=nokogiri version=1.18.3 platform=ruby> because it is missing extensions
```

peuvent être résolus en exécutant :

```shell
gem pristine <module>
bundle install
```

<br/>

## Mise en forme

- Utilisation de [Minima](https://github.com/jekyll/minima#readme)
- L'ordre des onglets est déterminé par le nom des fichiers ; vous pouvez donc leur ajouter le préfixe `a_`, etc.
- Liste des polices : https://fonts.google.com
- L'emplacement des fichiers de Minima peut être trouvé avec `bundle show minima`. 



<br/>

## Admonitions :

L'ajout de ce qui suit au groupe `jekyll_plugins` dans le `gemfile` active les admonitions dans les fichiers Markdown :

```
  gem "jekyll-gfm-admonitions"
```

Les admonitions peuvent être créées ainsi :

```markdown
> [!NOTE] 
> Note text line1
> Note text line2
```

Les admonitions disponibles sont :


```markdown
[!NOTE], [!TIP], [!WARNING], [!CAUTION], [!IMPORTANT]
```

<br/>




## Ajout de contenu

Les fichiers situés dans des répertoires dont le nom commence par un tiret bas
ne sont pas traités par Jekyll s'ils sont spécifiés dans le fichier _config.yml comme ceci :

```markdown
# this add content to the website from the local dirs starting with _
collections:
  pi0:
    output: true
```

<br/>

Des [permaliens](https://jekyllrb.com/docs/permalinks/) peuvent éventuellement être ajoutés pour la navigation.


<br/>

## Fonctionnalités Markdown supplémentaires

- Liens web : 
```
This site was built using [GitHub Pages](https://pages.github.com/).
```

- Liens vers des sections :
```
See the [Admonitions](#admonitions) section for more details.
```

- Adresses électroniques :
```
You can contact me at [gemc@jlab.org](mailto:gemc@jlab.org)
```

<br/>




<br/>

## Liens utiles :

- [Jekyll sur GitHub](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [Tutoriel Jekyll](https://jekyllrb.com/docs/step-by-step/01-setup/)
- [Tableaux sympas](https://github.com/jeffreytse/jekyll-spaceship)
