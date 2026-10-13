---
layout: default
title: "Various macOS Notes"
permalink: /mynotes/macos.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# macOS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## Autenticazione disabilitata

Il problema potrebbe essere dovuto a un token sicuro danneggiato.

Per disabilitare e riabilitare i token, e quindi aggiornare `/` con `diskutil`, esegui i seguenti comandi.
Nota che il `-` indica al comando di richiedere le password. Sostituirlo con le password effettive potrebbe
richiedere alcuni caratteri di escape (ad esempio per `&`).

```shell
sysadminctl -secureTokenStatus <username>
sysadminctl -secureTokenOff <username> -password - -adminUser <adminusername> -adminPassword -
sysadminctl -secureTokenOn <username> -password - -adminUser <adminusername> -adminPassword -
diskutil apfs UpdatePreboot /
```
