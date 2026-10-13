---
layout: default
title: "python notes"
permalink: /mynotes/python.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Python 笔记
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>




## 环境

要创建并使用新的 Python 环境，并安装特定的包，
请参阅下面的两个示例：

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




- 退出 Python 环境：`deactivate`
- 列出所有已安装的包：`pip list`
- 更新已安装的包：`pip install --upgrade pip`
- 卸载某个包：`pip uninstall <package_name>`


<br/>


## 如何发布到 PyPI

对于基于 `pyproject.toml` 构建、并通过 GitHub Actions 使用 PyPI 可信发布（trusted publishing）
机制发布的 Python 包，请采用此工作流。

### 1. 准备包

确保 `pyproject.toml` 中配置了项目元数据、README、许可证文件、
依赖项、可选依赖项以及构建后端。对于自定义许可证，
除非该许可证确实经过 OSI 批准，否则不要声明 OSI Trove 分类标识：

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

上面的 `tag-pattern` 表示，只有像 `v0.2.0` 这样的稳定标签才用于确定包的
版本。指向会发生变化的 `dev` 标签在确定包版本时会被忽略。

### 2. 配置可信发布

在 PyPI 和 TestPyPI 中，添加一个与 GitHub
工作流匹配的待生效可信发布者（pending trusted publisher）：

对于 [TestPyPI 可信发布者](https://test.pypi.org/manage/account/publishing/)：

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: testpypi
```

对于 [PyPI 可信发布者](https://pypi.org/manage/account/publishing/)：

```text
PyPI project name: pygemc
Owner: gemc
Repository name: pygemc
Workflow name: publish_pypi.yml
Environment name: pypi
```

GitHub 工作流应将环境设置为与发布目标匹配：

{% raw %}
```yaml
jobs:
  publish:
    runs-on: ubuntu-latest
    environment: ${{ inputs.repository }}
```
{% endraw %}

### 3. 创建稳定发布标签


### 4. 从 GitHub Actions 手动发布

手动运行 `Publish PyPI` 工作流。

首先发布到 TestPyPI：

```text
ref: v0.2.0
repository: testpypi
```

然后，如果包看起来正确，再发布到 PyPI：

```text
ref: v0.2.0
repository: pypi
```

该工作流应拒绝分支、`dev` 以及非稳定标签。例如，
只允许匹配以下模式的标签：

```text
^v[0-9]+\.[0-9]+\.[0-9]+$
```

### 5. 验证发布

检查 PyPI 是否能找到该包：

```shell
python -m pip index versions pygemc
```

在一个全新的虚拟环境中安装：

```shell
python3 -m venv /tmp/pygemc-check
source /tmp/pygemc-check/bin/activate
python -m pip install --upgrade pip
python -m pip install pygemc
python -c "import pygemc; print(pygemc.__name__)"
```

对于 TestPyPI，请将 PyPI 保留为额外索引，以便仍能找到
常规依赖项：

```shell
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple \
  pygemc
```
