---
layout: default
title: "Various macOS Notes"
---
{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# macOS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## Authentication Disabled

This may be due to a corrupt secure token.

To disable and re-enable the tokens, and then update `/` with `diskutil`, run the following commands.
Notice the `-` will tell the command to prompt for the passwords. Replacing it with the actual passwords may need
some escape char (for example for `&`).

```shell
sysadminctl -secureTokenStatus <username>
sysadminctl -secureTokenOff <username> -password - -adminUser <adminusername> -adminPassword -
sysadminctl -secureTokenOn <username> -password - -adminUser <adminusername> -adminPassword -
diskutil apfs UpdatePreboot /
```
