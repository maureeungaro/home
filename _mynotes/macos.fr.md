---
layout: default
title: "Various macOS Notes"
permalink: /mynotes/macos.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# macOS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## Authentification désactivée

Cela peut être dû à un jeton sécurisé (secure token) corrompu.

Pour désactiver puis réactiver les jetons, et ensuite mettre à jour `/` avec `diskutil`, exécutez les commandes
suivantes. Notez que le `-` indique à la commande de demander les mots de passe. Le remplacer par les
mots de passe réels peut nécessiter des caractères d'échappement (par exemple pour `&`).

```shell
sysadminctl -secureTokenStatus <username>
sysadminctl -secureTokenOff <username> -password - -adminUser <adminusername> -adminPassword -
sysadminctl -secureTokenOn <username> -password - -adminUser <adminusername> -adminPassword -
diskutil apfs UpdatePreboot /
```
