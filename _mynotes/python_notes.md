---
layout: default
title: "jekyll"
---
{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# Python Notes
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>




## Environment

To define and use a new python environment, and install particular packages, 
see the following couple of examples:

### Meson

```shell
python3 -m venv ~/venv/meson
source ~/venv/meson/bin/activate
pip install 'meson @ git+https://github.com/mesonbuild/meson.git'
meson --version
```

<br/>

### Pyvista

```shell
python3 -m venv ~/venv/pyvista/
source ~/venv/pyvista/bin/activate
pip install pyvista vtk pyqt6 pyvistaqt
```


To exit from the python environment: `deactivate`