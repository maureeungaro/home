---
layout: default
title: "python notes"
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




- To exit from the python environment: `deactivate`
- To list all the installed packages: `pip list`
- To update the installed packages: `pip install --upgrade pip`
- To uninstall a package: `pip uninstall <package_name>`


<br/>


## How to Publish to PyPI

Use this workflow for a Python package that is built from `pyproject.toml` and
published by GitHub Actions using PyPI trusted publishing.

### 1. Prepare the package

Make sure `pyproject.toml` has the project metadata, README, license file,
dependencies, optional dependencies, and build backend configured. For a custom
license, avoid declaring an OSI trove classifier unless the license is actually
OSI-approved:

```toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"

[project]
name = "pygemc"
dynamic = ["version"]
readme = "README.md"
license = { file = "LICENSE.md" }
requires-python = ">=3.10"

[tool.hatch.version]
source = "vcs"
tag-pattern = "^v(?P<version>\\d+\\.\\d+\\.\\d+)$"
```

The `tag-pattern` above means only stable tags such as `v0.2.0` define package
versions. A moving `dev` tag is ignored for package versioning.

### 2. Configure trusted publishing

In PyPI and TestPyPI, add a pending trusted publisher matching the GitHub
workflow:

For [TestPyPI trusted publishers](https://test.pypi.org/manage/account/publishing/):

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: testpypi
```

For [PyPI trusted publishers](https://pypi.org/manage/account/publishing/):

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: pypi
```

The GitHub workflow should set the environment to match the target:

{% raw %}
```yaml
jobs:
  publish:
    runs-on: ubuntu-latest
    environment: ${{ inputs.repository }}
```
{% endraw %}

### 3. Create the stable release tag


### 4. Publish manually from GitHub Actions

Run the `Publish PyPI` workflow manually.

First publish to TestPyPI:

```text
ref: v0.2.0
repository: testpypi
```

Then, if the package looks correct, publish to PyPI:

```text
ref: v0.2.0
repository: pypi
```

The workflow should reject branches, `dev`, and non-stable tags. For example,
allow only tags matching:

```text
^v[0-9]+\.[0-9]+\.[0-9]+$
```

### 5. Verify the release

Check that PyPI sees the package:

```shell
python -m pip index versions pygemc
```

Install in a fresh virtual environment:

```shell
python3 -m venv /tmp/pygemc-check
source /tmp/pygemc-check/bin/activate
python -m pip install --upgrade pip
python -m pip install pygemc
python -c "import pygemc; print(pygemc.__name__)"
```

For TestPyPI, keep PyPI as an extra index so normal dependencies can still be
found:

```shell
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple \
  pygemc
```
