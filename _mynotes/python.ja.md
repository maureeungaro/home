---
layout: default
title: "python notes"
permalink: /mynotes/python.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Python ノート
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>




## 環境

新しい Python 環境を作成して使用し、特定のパッケージをインストールする方法については、
次の 2 つの例を参照してください。

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




- Python 環境から抜けるには: `deactivate`
- インストール済みのパッケージをすべて一覧表示するには: `pip list`
- インストール済みのパッケージを更新するには: `pip install --upgrade pip`
- パッケージをアンインストールするには: `pip uninstall <package_name>`


<br/>


## PyPI への公開方法

`pyproject.toml` からビルドし、PyPI のトラステッドパブリッシングを使って
GitHub Actions で公開する Python パッケージには、このワークフローを使用してください。

### 1. パッケージを準備する

`pyproject.toml` にプロジェクトのメタデータ、README、ライセンスファイル、
依存関係、オプションの依存関係、ビルドバックエンドが設定されていることを確認してください。
独自のライセンスの場合は、そのライセンスが実際に OSI の承認を受けていない限り、
OSI の Trove 分類子を指定しないようにしてください。

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

上記の `tag-pattern` は、`v0.2.0` のような安定版タグのみがパッケージのバージョンを定義することを意味します。
参照先が更新される `dev` タグは、パッケージのバージョン決定では無視されます。

### 2. トラステッドパブリッシングを構成する

PyPI と TestPyPI で、GitHub ワークフローに一致する保留中のトラステッドパブリッシャーを
追加してください。

[TestPyPI のトラステッドパブリッシャー](https://test.pypi.org/manage/account/publishing/)の場合:

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: testpypi
```

[PyPI のトラステッドパブリッシャー](https://pypi.org/manage/account/publishing/)の場合:

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: pypi
```

GitHub ワークフローでは、公開先に対応する環境を設定する必要があります。

{% raw %}
```yaml
jobs:
  publish:
    runs-on: ubuntu-latest
    environment: ${{ inputs.repository }}
```
{% endraw %}

### 3. 安定版リリースタグを作成する


### 4. GitHub Actions から手動で公開する

`Publish PyPI` ワークフローを手動で実行します。

まず TestPyPI に公開します。

```text
ref: v0.2.0
repository: testpypi
```

次に、パッケージに問題がなければ、PyPI に公開します。

```text
ref: v0.2.0
repository: pypi
```

ワークフローでは、ブランチ、`dev`、および安定版ではないタグを拒否する必要があります。たとえば、
次のパターンに一致するタグのみを許可します。

```text
^v[0-9]+\.[0-9]+\.[0-9]+$
```

### 5. リリースを検証する

PyPI でパッケージが認識されていることを確認します。

```shell
python -m pip index versions pygemc
```

新しい仮想環境にインストールします。

```shell
python3 -m venv /tmp/pygemc-check
source /tmp/pygemc-check/bin/activate
python -m pip install --upgrade pip
python -m pip install pygemc
python -c "import pygemc; print(pygemc.__name__)"
```

TestPyPI の場合は、通常の依存パッケージを引き続き検索できるように、PyPI を追加の
インデックスとして指定しておきます。

```shell
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple \
  pygemc
```
