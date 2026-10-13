---
layout: default
title: "Using Jekyll"
permalink: /mynotes/jekyll.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Jekyll を使う
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

- [Jekyll ホーム](https://jekyllrb.com)

## 各種コマンド: 

Jekyll サーバーの起動、クリーンアップ、更新、バンドルのインストールを行うには、次を実行します:

```shell
bundle exec jekyll serve
bundle exec jekyll clean 
bundle update jekyll
bundle install
```

- gemfile を変更した場合は、`bundle` を実行する必要があります
- 設定 YAML を変更した場合（たとえばテーマを更新した場合）は、`bundle update` を実行する必要があります

<br/>

> [!CAUTION]
> `Gemfile.lock` が別のバージョンの Bundler を指定していることがあります。次のコマンドで確認してください:
> 
> ```bash
> gem list bundler
> tail -n +1 Gemfile.lock | sed -n '/BUNDLED WITH/,$p'
> ```
> このファイルを削除すると問題が解決します。

> [!IMPORTANT] 
> bundle は絶対に `sudo` で実行しないでください

<br/>

Bundler を使用中の Ruby と互換性のあるバージョンに更新し、古いバージョンを確認／アンインストールするには:

```shell
sudo gem update --system
sudo gem update bundler
sudo gem install bundler 
gem list bundler    
sudo gem uninstall bundler -v 2.6.5
```

場合によっては、Bundler を完全に削除して再インストールします:

```shell
sudo rm -f /opt/homebrew/bin/bundle /opt/homebrew/bin/bundler
sudo gem uninstall bundler -aIx
```

<br/>


## 拡張機能の欠落

次のようなメッセージ:

```html
Source locally installed gems is ignoring #<Bundler::StubSpecification name=nokogiri version=1.18.3 platform=ruby> because it is missing extensions
```

には、次を実行することで対処できます:

```shell
gem pristine <module>
bundle install
```

<br/>

## スタイル設定

- [Minima](https://github.com/jekyll/minima#readme) を使用しています
- タブの順序はファイル名で決まるため、`a_` などを先頭に付けることができます
- フォント一覧: https://fonts.google.com
- minima のファイルの場所は `bundle show minima` で確認できます。



<br/>

## 注意書き（Admonitions）:

`gemfile` の `jekyll_plugins` グループに次を追加すると、Markdown ファイルで注意書きが有効になります:

```
  gem "jekyll-gfm-admonitions"
```

注意書きは次のように記述できます:

```markdown
> [!NOTE] 
> Note text line1
> Note text line2
```

利用可能な注意書きは次のとおりです:


```markdown
[!NOTE], [!TIP], [!WARNING], [!CAUTION], [!IMPORTANT]
```

<br/>




## コンテンツの追加

アンダースコアで始まるディレクトリ内のファイルは、
_config.yml ファイルで次のように指定されている場合、Jekyll によって処理されません:

```markdown
# this add content to the website from the local dirs starting with _
collections:
  pi0:
    output: true
```

<br/>

必要に応じて、ナビゲーション用に[パーマリンク](https://jekyllrb.com/docs/permalinks/)を追加できます。


<br/>

## その他の Markdown 機能

- Web リンク: 
```
This site was built using [GitHub Pages](https://pages.github.com/).
```

- セクションへのリンク:
```
See the [Admonitions](#admonitions) section for more details.
```

- メール:
```
You can contact me at [gemc@jlab.org](mailto:gemc@jlab.org)
```

<br/>




<br/>

## 便利なリンク:

- [GitHub 上の Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [Jekyll チュートリアル](https://jekyllrb.com/docs/step-by-step/01-setup/)
- [見栄えのよい表](https://github.com/jeffreytse/jekyll-spaceship)
