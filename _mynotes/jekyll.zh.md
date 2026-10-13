---
layout: default
title: "Using Jekyll"
permalink: /mynotes/jekyll.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# 使用 Jekyll
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

- [Jekyll 主页](https://jekyllrb.com)

## 各类命令： 

要启动 Jekyll 服务器、清理、更新、安装依赖包，请运行：

```shell
bundle exec jekyll serve
bundle exec jekyll clean 
bundle update jekyll
bundle install
```

- 如果修改了 gemfile，需要运行 `bundle`
- 如果修改了 YAML 配置文件（例如更新主题），需要运行 `bundle update`

<br/>

> [!CAUTION]
> 有时 `Gemfile.lock` 会锁定一个不同版本的 Bundler。请核实：
> 
> ```bash
> gem list bundler
> tail -n +1 Gemfile.lock | sed -n '/BUNDLED WITH/,$p'
> ```
> 删除该文件即可解决问题。

> [!IMPORTANT] 
> 千万不要用 `sudo` 运行 bundle

<br/>

要将 Bundler 更新到与你的 Ruby 版本兼容的版本，并检查 / 卸载旧版本：

```shell
sudo gem update --system
sudo gem update bundler
sudo gem install bundler 
gem list bundler    
sudo gem uninstall bundler -v 2.6.5
```

有时需要彻底清除 Bundler 并重新安装：

```shell
sudo rm -f /opt/homebrew/bin/bundle /opt/homebrew/bin/bundler
sudo gem uninstall bundler -aIx
```

<br/>


## 缺失的扩展

以下这类消息：

```html
Source locally installed gems is ignoring #<Bundler::StubSpecification name=nokogiri version=1.18.3 platform=ruby> because it is missing extensions
```

可以通过执行以下命令来解决：

```shell
gem pristine <module>
bundle install
```

<br/>

## 样式

- 使用 [Minima](https://github.com/jekyll/minima#readme)
- 标签页顺序由文件名决定，因此你可以在文件名前加上 `a_` 等前缀。
- 字体列表：https://fonts.google.com
- minima 文件的位置可以通过 `bundle show minima` 找到。 



<br/>

## 提示框（Admonitions）：

将以下内容添加到 `gemfile` 中的 `jekyll_plugins` 分组，即可在 Markdown 文件中启用提示框：

```
  gem "jekyll-gfm-admonitions"
```

提示框可以这样实现：

```markdown
> [!NOTE] 
> Note text line1
> Note text line2
```

可用的提示框类型有：


```markdown
[!NOTE], [!TIP], [!WARNING], [!CAUTION], [!IMPORTANT]
```

<br/>




## 添加内容

对于以下划线开头的目录中的文件，
如果在 _config.yml 文件中按如下方式指定，Jekyll 将不会处理它们：

```markdown
# this add content to the website from the local dirs starting with _
collections:
  pi0:
    output: true
```

<br/>

可以选择性地添加[固定链接（permalinks）](https://jekyllrb.com/docs/permalinks/)以便于导航。


<br/>

## 其他 Markdown 功能

- 网页链接： 
```
This site was built using [GitHub Pages](https://pages.github.com/).
```

- 章节链接：
```
See the [Admonitions](#admonitions) section for more details.
```

- 电子邮件：
```
You can contact me at [gemc@jlab.org](mailto:gemc@jlab.org)
```

<br/>




<br/>

## 实用链接：

- [GitHub 上的 Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [Jekyll 教程](https://jekyllrb.com/docs/step-by-step/01-setup/)
- [漂亮的表格](https://github.com/jeffreytse/jekyll-spaceship)
