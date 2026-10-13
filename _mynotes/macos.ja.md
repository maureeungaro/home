---
layout: default
title: "Various macOS Notes"
permalink: /mynotes/macos.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# macOS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## 認証が無効化されている

これは、セキュアトークンが破損していることが原因の可能性があります。

トークンを無効化してから再度有効化し、その後 `diskutil` で `/` を更新するには、以下のコマンドを実行してください。
`-` を指定するとコマンドがパスワードの入力を求める点に注意してください。これを実際のパスワードに置き換える場合は、
エスケープ文字が必要になることがあります（例えば `&` の場合など）。

```shell
sysadminctl -secureTokenStatus <username>
sysadminctl -secureTokenOff <username> -password - -adminUser <adminusername> -adminPassword -
sysadminctl -secureTokenOn <username> -password - -adminUser <adminusername> -adminPassword -
diskutil apfs UpdatePreboot /
```
