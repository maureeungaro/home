---
layout: default
title: "python notes"
permalink: /mynotes/python.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Notes Python
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>




## Environnement

Pour créer et utiliser un nouvel environnement Python et installer des paquets spécifiques,
consultez les deux exemples suivants :

### Meson

```shell
python3 -m venv ~/venv/meson
source ~/venv/meson/bin/activate
pip install 'meson @ git+https://github.com/mesonbuild/meson.git'
meson --version
```

<br/>

### PyVista

```shell
python3 -m venv ~/venv/pyvista/
source ~/venv/pyvista/bin/activate
pip install pyvista vtk pyqt6 pyvistaqt
```




- Pour quitter l'environnement Python : `deactivate`
- Pour lister tous les paquets installés : `pip list`
- Pour mettre à jour les paquets installés : `pip install --upgrade pip`
- Pour désinstaller un paquet : `pip uninstall <package_name>`


<br/>


## Comment publier sur PyPI

Utilisez ce workflow pour un paquet Python construit à partir de `pyproject.toml` et
publié par GitHub Actions à l'aide de la publication de confiance de PyPI.

### 1. Préparer le paquet

Assurez-vous que les métadonnées du projet, le README, le fichier de licence,
les dépendances, les dépendances optionnelles et le backend de construction sont configurés
dans `pyproject.toml`. Pour une licence personnalisée, évitez de déclarer un classificateur Trove
indiquant une approbation par l'OSI, sauf si la licence est effectivement approuvée par l'OSI :

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

Le `tag-pattern` ci-dessus signifie que seuls les tags stables tels que `v0.2.0` définissent
les versions du paquet. Un tag `dev` dont la cible évolue est ignoré pour le versionnement du paquet.

### 2. Configurer la publication de confiance

Dans PyPI et TestPyPI, ajoutez un éditeur de confiance en attente correspondant au
workflow GitHub :

Pour les [éditeurs de confiance de TestPyPI](https://test.pypi.org/manage/account/publishing/) :

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: testpypi
```

Pour les [éditeurs de confiance de PyPI](https://pypi.org/manage/account/publishing/) :

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: pypi
```

Le workflow GitHub doit définir l'environnement pour qu'il corresponde à la cible :

{% raw %}
```yaml
jobs:
  publish:
    runs-on: ubuntu-latest
    environment: ${{ inputs.repository }}
```
{% endraw %}

### 3. Créer le tag de la version stable


### 4. Publier manuellement depuis GitHub Actions

Exécutez manuellement le workflow `Publish PyPI`.

Publiez d'abord sur TestPyPI :

```text
ref: v0.2.0
repository: testpypi
```

Ensuite, si le paquet semble correct, publiez sur PyPI :

```text
ref: v0.2.0
repository: pypi
```

Le workflow doit rejeter les branches, `dev` et les tags non stables. Par exemple,
n'autorisez que les tags correspondant à :

```text
^v[0-9]+\.[0-9]+\.[0-9]+$
```

### 5. Vérifier la version publiée

Vérifiez que le paquet est disponible sur PyPI :

```shell
python -m pip index versions pygemc
```

Installez-le dans un nouvel environnement virtuel :

```shell
python3 -m venv /tmp/pygemc-check
source /tmp/pygemc-check/bin/activate
python -m pip install --upgrade pip
python -m pip install pygemc
python -c "import pygemc; print(pygemc.__name__)"
```

Pour TestPyPI, conservez PyPI comme index supplémentaire afin que les dépendances habituelles puissent
toujours être trouvées :

```shell
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple \
  pygemc
```
