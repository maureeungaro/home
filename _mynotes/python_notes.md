---
layout: default
title: "jekyll"
---
{% include mynotes.html %}


# Python Notes
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>




## Environment

To define and use a new python environment, and install particular packages:

```shell
python3 -m venv .venv-meson
. .venv-meson/bin/activate
pip install 'meson @ git+https://github.com/mesonbuild/meson.git'
meson --version
```