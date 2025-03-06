---
layout: default
title: "jekyll"
---

# [Jekyll](https://jekyllrb.com)

---

<br/>


## Various commands: 

```
bundle exec jekyll serve
bundle exec jekyll clean 
bundle update jekyll
bundle install
```

- If the gemfile is changed, need to run `bundle`
- If the config yaml is changed, (for example update theme), need to update `bundle update`

<br/>

---

<br/>

## Theme [Minima](https://github.com/jekyll/minima#readme) notes

- The tab order is given by the filename, so you can prepend `a_` etc.
- List of Fonts: https://fonts.google.com

<br/>

---

<br/>

## Adding Content

The files in directories starting with an underscore
are not processed by jekyll if specified in the _config.yml file like this:

```
# this add content to the website from the local dirs starting with _
collections:
  pi0:
    output: true
```

<br/>

Optionally [permalinks](https://jekyllrb.com/docs/permalinks/) can be added for navigation.

<br/>

---

<br/>

## Useful links:

- [versions](https://pages.github.com/versions/)  for the compatible version of the software when running jekyll on github
- [jekyll on github](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [jekyll tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/).
- [cool tables](https://github.com/jeffreytse/jekyll-spaceship)
