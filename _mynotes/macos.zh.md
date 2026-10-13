---
layout: default
title: "Various macOS Notes"
permalink: /mynotes/macos.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# macOS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## 身份验证被禁用

这可能是由于安全令牌损坏所致。

要先禁用再重新启用令牌，然后使用 `diskutil` 更新 `/`，请运行以下命令。
请注意，`-` 会让命令提示输入密码。如果用实际密码替换它，可能需要
一些转义字符（例如针对 `&`）。

```shell
sysadminctl -secureTokenStatus <username>
sysadminctl -secureTokenOff <username> -password - -adminUser <adminusername> -adminPassword -
sysadminctl -secureTokenOn <username> -password - -adminUser <adminusername> -adminPassword -
diskutil apfs UpdatePreboot /
```
