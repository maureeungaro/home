## Run from 'home' directory:

`bundle exec jekyll serve`


## To install [jekyll](https://jekyllrb.com):

It can be done with ruby. 
The ruby-install ruby can be skipped, can use brew to overwrite the old system version,
for example 

```
brew install ruby@3.0
brewDir=$(brew --prefix)
if [ -d $brewDir ]; then
	export PATH=$brewDir/opt/ruby@3.0/bin:$PATH
fi
```
 
 
```
brew install chruby ruby-install  
(sudo) gem install jekyll
```

## Create a new site:

Check the [quickstart](https://jekyllrb.com).


## [Minima](https://github.com/jekyll/minima#readme) Motes

- The tab order is given by the filename, so you can prepend `a_` etc.
- See 'layouts' for the 4 choices



## ICONS

https://feathericons.com
https://realfavicongenerator.net


## GH-PAGES

https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll

Remember to use the exact dependencies that are used on GitHub:

https://pages.github.com/versions/


## Modifying default Style

Use a file assets/main.scss with the following content:


```
---
---

@import "{{ site.theme }}";

<your settings here>

```

## Adding Content

The files in directories starting with an underscore
are not processed by jekyll if specified in the _config.yml file like this:

```
# this add content to the website from the local dirs starting with _
collections:
  pi0:
    output: true
```

Optionally [permalinks](https://jekyllrb.com/docs/permalinks/) can be added for navigation.