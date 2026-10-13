---
layout: default
title: "python notes"
permalink: /mynotes/python.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Note su Python
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>




## Ambiente

Per creare e utilizzare un nuovo ambiente Python e installare pacchetti specifici,
consulta i due esempi seguenti:

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




- Per uscire dall'ambiente Python: `deactivate`
- Per elencare tutti i pacchetti installati: `pip list`
- Per aggiornare i pacchetti installati: `pip install --upgrade pip`
- Per disinstallare un pacchetto: `pip uninstall <package_name>`


<br/>


## Come pubblicare su PyPI

Usa questo flusso di lavoro per un pacchetto Python generato a partire da `pyproject.toml` e
pubblicato tramite GitHub Actions utilizzando il trusted publishing di PyPI.

### 1. Prepara il pacchetto

Assicurati che in `pyproject.toml` siano configurati i metadati del progetto, il README, il file di licenza,
le dipendenze, le dipendenze opzionali e il backend di build. Per una licenza personalizzata,
evita di dichiarare un classificatore Trove OSI a meno che la licenza non sia
effettivamente approvata da OSI:

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

Il `tag-pattern` riportato sopra indica che solo i tag stabili come `v0.2.0` definiscono le versioni
del pacchetto. Un tag `dev` aggiornato nel tempo viene ignorato per il versionamento del pacchetto.

### 2. Configura il trusted publishing

Su PyPI e TestPyPI, aggiungi un trusted publisher in attesa di attivazione corrispondente al
workflow di GitHub:

Per i [trusted publisher di TestPyPI](https://test.pypi.org/manage/account/publishing/):

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: testpypi
```

Per i [trusted publisher di PyPI](https://pypi.org/manage/account/publishing/):

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: pypi
```

Il workflow di GitHub dovrebbe impostare l'ambiente in modo che corrisponda alla destinazione:

{% raw %}
```yaml
jobs:
  publish:
    runs-on: ubuntu-latest
    environment: ${{ inputs.repository }}
```
{% endraw %}

### 3. Crea il tag della release stabile


### 4. Pubblica manualmente da GitHub Actions

Esegui manualmente il workflow `Publish PyPI`.

Prima pubblica su TestPyPI:

```text
ref: v0.2.0
repository: testpypi
```

Poi, se il pacchetto risulta corretto, pubblica su PyPI:

```text
ref: v0.2.0
repository: pypi
```

Il workflow dovrebbe rifiutare i branch, `dev` e i tag non stabili. Ad esempio,
consenti solo i tag corrispondenti a:

```text
^v[0-9]+\.[0-9]+\.[0-9]+$
```

### 5. Verifica la release

Controlla che il pacchetto sia visibile su PyPI:

```shell
python -m pip index versions pygemc
```

Installa in un nuovo ambiente virtuale:

```shell
python3 -m venv /tmp/pygemc-check
source /tmp/pygemc-check/bin/activate
python -m pip install --upgrade pip
python -m pip install pygemc
python -c "import pygemc; print(pygemc.__name__)"
```

Per TestPyPI, mantieni PyPI come indice aggiuntivo in modo che le normali dipendenze possano
continuare a essere trovate:

```shell
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple \
  pygemc
```
