## Run from 'home' directory:

`bundle exec jekyll serve`

- If the gemfile is changed, need to run `bundle`
- If the config yaml is changed, (for example update theme), need to update `bundle update`



#### Plots and slides are updated on jlabl4 by the cronjob `update_mauriplots_jlabl4` 

in the `[pubs]` repo. to copy:

```
scp /opt/projects/pubs/update_mauriplots_jlabl4.zsh ifarm:.
```

# Versions:

See https://pages.github.com/versions/  for the compatible version of the software when running jekyll on github


#### Link checker:

https://www.deadlinkchecker.com/



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


## Theme [Minima](https://github.com/jekyll/minima#readme) notes

- The tab order is given by the filename, so you can prepend `a_` etc.
- Fonts: https://fonts.google.com



## Icons and html symbols

https://feathericons.com (need download to use)<br/>

https://icons8.com

https://www.w3schools.com/charsets/ref_utf_arrows.asp


## GH-Pages

### From repository:

- Recommended: Settings > Pages
- Source: Github Actions. If new, accept standard yaml.
This will create a  .github/workflows/jekyll.yml file.

### In general (not recommended)

https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll

Remember to use the exact dependencies that are used on GitHub:

https://pages.github.com/versions/




# Twitter links:

Use https://publish.twitter.com/#




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