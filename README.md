## Run from 'home' directory:

`bundle exec jekyll serve`

## To install jekyll:

It can be done with ruby
 
```
brew install chruby ruby-install  
sudo gem install jekyll
```

## To create a new Gemfile:

```
bundle init
bundle add jekyll
```

may need ro run `bundle install` to install missing gems

## Create a new site:

Follow the [jekyll tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/).

At the editing the Gemfile step, add

gem "github-pages", "~> 227", group: :jekyll_plugins

check the [dependency versions](https://pages.github.com/versions/) 

Copy most files from a previous project:

```
_config.yml
_content/
_includes/
_layouts/
_sass/
_site/
assets/
```


## ICONS

https://feathericons.com



## GH-PAGES

https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll

