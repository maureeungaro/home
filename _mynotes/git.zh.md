---
layout: default
title: "Using Git"
permalink: /mynotes/git.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# 使用 Git
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## 浅克隆单个分支或标签及其子模块，不包含完整历史

```shell
git clone -b v1.2.3 --recurse-submodules --shallow-submodules --depth 1 [repo] 
```

<br/>

## Git LFS（大文件存储）

安装 Git LFS，然后为你的用户账户执行一次初始化：

```shell
# macOS
brew install git-lfs

# Ubuntu/Debian
sudo apt install git-lfs

git lfs install
```

在仓库中启用 Git LFS，并选择要用它存储的文件类型：

```shell
cd path/to/repository
git lfs track "*.zip"       # use a pattern or a specific file path
git add .gitattributes      # commit the tracking rules
git add path/to/archive.zip
git commit -m "Track ZIP files with Git LFS"
git push
```

运行 `git lfs ls-files` 可列出已跟踪的文件。跟踪某个模式只会影响新添加的文件；若要将已提交到常规 Git 的文件
迁移到 LFS，则需使用 `git lfs migrate`，该命令会重写仓库历史。

<br/>

## 发布不可变的发布版本并移动其主版本标签

为带版本的 GitHub Action 或其他项目使用两个标签：

* `v1.0.1` 是不可变的发布标签。切勿移动或复用它。
* `v1` 是可移动的兼容性标签。指定 `uses: owner/repository@v1` 的用户会获取最新的
  兼容 `v1.x.x` 版本。

GitHub Release 必须始终关联到 `v1.0.1`。只有 `v1` 标签会移动；不存在单独的可移动
GitHub Release。

#### 1) 发布 GitHub Release

在仓库的 GitHub 页面上：

1. 打开 **Releases** 并选择 **Draft a new release**。
2. 创建（或选择）`v1.0.1` 标签。
3. 添加发布标题、说明和所需的附件。


#### 2) 创建或更新主版本标签

设置不可变的版本号和可移动的主版本号：

```shell
version=v1.0.1
major=v1
```

只有在 `v1.0.1` 的 GitHub Release 发布之后，才将 `v1` 指向它。首次发布时，这会创建
`v1`；在此后的每次发布（`v1.0.2`、`v1.1.2`……）中，同一条命令会把 `v1` 更新到最新的不可变
标签。获取 GitHub 刚创建的标签，将本地 `v1` 标签指向 `$version` 所引用的提交，然后
仅强制更新 GitHub 上的该标签：

```shell
git fetch origin tag "$version"
git tag -f "$major" "$version^{}"
git push --force origin "refs/tags/$major"
```

`^{}` 后缀会对版本标签解引用，因此 `v1` 直接指向发布提交。必须使用强制更新，
因为移动标签属于非快进更新（首次操作时，`v1` 尚不存在，使用强制更新也无妨）。
使用 GitHub 标签规则集保护 `v*.*.*` 这类不可变标签，同时允许需要移动的主版本标签更新。

<br/>

## 更新标签 / 发布版本（重写已有标签）

**使用以下变量**

* `tag`：GitHub 标签名（例如 `v1.2.3`）
* `btag`：从该标签创建的临时分支名
* `rtag`：完整的标签引用路径（`refs/tags/<tag>`），用于远程删除

示例：`tag=v1.2.3`

```shell
btag="b$tag"
rtag="refs/tags/$tag"
```

#### 1) 从已有标签创建并切换到临时分支

```shell
git fetch origin --tags
git switch -c "$btag" "$tag"
```

#### 2) 进行修改、提交，并推送临时分支

```shell
git commit -am "Fixes for $tag"
git push -u origin "$btag"
```

#### 3) 删除指向旧提交的本地标签，并在新的 HEAD 处重新创建该标签

（你已经在 `$btag` 上，因此无需再执行 `git switch "$btag"`。）

```shell
git tag -d "$tag"
git tag "$tag"
```

#### 4) 替换远程标签，使其指向新提交

先删除旧的远程标签，再推送新标签。
显式强制更新远程标签，因为按惯例标签是不可变的，许多服务器会拒绝未使用强制选项的非快进标签更新。

```shell
git push origin ":$rtag"
git push --force origin "$rtag"
```

#### 5) 如有必要，更新 GitHub Release（及其附件）
* 如果你上传过发布附件（二进制文件 / 自定义 .tar.gz / 等）：
   删除旧附件并上传新附件，以更新现有发布版本（或删除并重新创建该发布版本）。
   移动标签不会替换已上传的附件。
* 如果只使用 GitHub 自动生成的源码归档（“Source code (tar.gz/zip)”）：
  通常可以保持发布版本原样；它仍然对应 $tag，生成的归档会
  随标签更新（由于缓存，可能需要稍等片刻）。
* 如果需要更改发布说明/变更日志：
  可以编辑现有的发布说明，或删除并重新创建 $tag 对应的发布版本。

#### 6) 清理：删除临时分支（远程 + 本地）

```shell
git push origin --delete "$btag"
git switch main
git branch -D "$btag"
```


<br/>

## 分支

创建新分支并切换到该分支：

```shell
git checkout -b branchname
```

切换到已有分支：

```shell
git checkout branchname
```

将 branch1 的更改合并到 branch2（其中一个可以是 main）。使用 `rebase` 可保持历史整洁。
也可以使用 `merge` 来保留两个分支的历史。
```shell
git checkout branch2
git merge/rebase branch1 
```

将分支推送到远程：

```shell
git push -u origin branchname
```

删除远程分支：

```shell
git push origin --delete branchname
```

列出所有远程分支：

- `git branch -r`：列出所有远程分支
- `git branch -a`：列出所有分支（本地和远程）
- `git branch -vv`：列出所有分支及其最新提交
- `git branch --merged`：列出已合并到当前分支的分支
- `git branch --no-merged`：列出尚未合并到当前分支的分支


<br/>

## 修改已有的拉取请求或合并请求

来自 **fork** 的 GitHub 拉取请求（PR）或 GitLab 合并请求（MR）会跟踪**该 fork 中的一个源分支**，
并提议将其合并到**原始仓库中的一个目标分支**（通常是 `main`）。fork
是一个独立的仓库，其中也包含分支。在同一个 fork 的同一分支上添加提交，
无论通过浏览器还是从本地克隆推送，都能自动更新尚未关闭的请求。
无需创建另一个请求。

### 在浏览器中更新代码

你无需克隆该 fork，但仍需有权限更新其源分支：作者可以编辑自己的 fork；
当作者在 GitHub 上启用 **Allow edits from maintainers**，或在 GitLab 上启用
**Allow contributions from members** 时，维护者也可以贡献更改。

1. 打开已有的 PR 或 MR，确认其**源 fork 和源分支**。
2. 在浏览器中打开该 fork 并选择源分支，例如 `my-feature`。
3. 打开文件并使用网页编辑器。对于涉及多个文件的更改，使用 GitHub 的网页编辑器或
   GitLab 的 Web IDE。
4. 审查更改并将其直接提交到**现有的源分支**。如果系统提供选项，
   请选择该分支，而不要创建新分支或新请求。

现有的 PR 或 MR 会自动包含这些提交。在请求页面上查看更新后的差异和
检查结果。

如果你有权限更新源分支，也可以直接在 PR 或 MR 上应用评审意见中的
修改建议。应用建议会在该分支上创建一个提交。
没有该权限的评审者可以提出修改建议，供作者或获授权的维护者应用。

### 从本地克隆更新代码

#### 1) 确认 fork 及其源分支

在请求页面上找到源 fork 和源分支，例如 `your-user/repository` 和 `my-feature`。
你需要对该 fork 的源分支拥有写权限。创建另一个 fork 或推送到其他分支
都不会更新现有请求。

在本地克隆中，查看每个远程指向哪个仓库：

```shell
git remote -v
```

以下命令使用名为 `fork` 的远程，指向请求的源 fork。如果该 fork 已经是你的
`origin`，请将以下命令中的 `fork` 全部替换为 `origin`。如果没有远程指向它，请使用 GitHub 或 GitLab 上该 fork 的
SSH 或 HTTPS 克隆 URL 添加一个远程：

```shell
git remote add fork <fork-clone-url>
```

#### 2) 切换到 fork 中的源分支

确保工作树干净：切换分支前，先提交或暂存（stash）所有无关更改。

```shell
git status
git fetch fork
git switch my-feature
# If the branch does not exist locally, use this instead:
# git switch --track fork/my-feature
git pull --ff-only fork my-feature
```

如果拉取操作报告分支出现分叉，请先整合本地与远程提交，再继续操作。

#### 3) 编辑文件、审查更改、提交，并推送到 fork

进行所需的更改并运行相关检查，然后：

```shell
git diff
git add path/to/file path/to/another-file
git diff --cached
git commit -m "Address review feedback"
git push fork HEAD:my-feature
```

`HEAD:my-feature` 会将当前提交推送到 fork 的现有源分支。原始仓库的
PR 或 MR 随即包含这些新提交。在请求页面上查看更新后的差异和检查结果。

#### 4) 如有需要，更新标题或描述

在 GitHub 或 GitLab 上打开现有请求并编辑其标题或描述。这些编辑
不需要 Git 提交。如果更改范围发生了变化，请描述最终的更改，以便评审者理解。

#### 如果你修订了提交或对源分支进行了变基

修订或变基已推送的提交会重写其历史。请先与共享该分支的其他人协调，
然后使用 `git push --force-with-lease fork HEAD:my-feature` 更新同一个请求。如果租约
检查拒绝推送，请先获取并审查远程更改，再重试。分支保护可能
禁止强制推送；添加新提交可避免重写历史。

请求合并后，后续更改应通过新分支和新的 PR 或 MR 提交。

<br/>

## 从另一个分支取出特定文件（不进行完整合并）

如果只需要另一个分支（或提交/标签）中的一个或几个文件，不要合并整个分支——
只将这些路径对应的文件复制到当前工作树。

> ⚠️ 这些命令会**覆盖**所列路径的本地副本。对这些文件所做的任何未提交更改都会
> 丢失。不确定时，请先运行 `git status`。

#### 先预览差异

```shell
git diff main..otherbranch -- path/to/file        # what would change in that file
git show otherbranch:path/to/file                 # print the file as it is on otherbranch
```

#### 复制文件（替换本地版本）

```shell
# Modern (recommended). --source can be a branch, tag, or commit SHA.
git restore --source=otherbranch --staged --worktree -- path/to/file [more/files...]

# Classic equivalent (also stages the result):
git checkout otherbranch -- path/to/file [more/files...]
```

`git checkout <branch> -- <path>` 会同时更新工作树和索引（更改已暂存）。
`git restore --source=<ref> -- <path>` 默认只更新工作树——添加 `--staged`（如上所示）
可同时暂存更改。然后照常提交：

```shell
git add path/to/file        # only needed if the file is not already staged
git commit -m "Bring path/to/file from otherbranch"
```

#### 只取文件中的部分更改（交互式，逐个差异块处理）

这是最接近“合并”单个文件的做法：选择要引入哪些差异块。

```shell
git restore -p --source=otherbranch -- path/to/file   # or: git checkout -p otherbranch -- path/to/file
```

#### 对单个文件进行真正的三方合并

`checkout`/`restore` 会*替换*文件，不会将其内容与你的文件内容合并。若要对同一文件的两个版本进行真正的
逐行合并，请使用 `git merge-file`：

```shell
git show otherbranch:path/to/file > /tmp/theirs       # their version
git show $(git merge-base HEAD otherbranch):path/to/file > /tmp/base   # common ancestor
git merge-file path/to/file /tmp/base /tmp/theirs     # merges into path/to/file, marks conflicts
```


<br/>

## 冲突

### 1. 解决冲突

- 查看哪些文件存在冲突：

```shell
git status
```

* **文本冲突（`UU` 等）**：打开文件并处理 `<<<<<<< ======= >>>>>>>` 冲突标记，然后：

```shell
git add path
```

* **保留其中一方**（选择 ours 或 theirs）：

```shell
git checkout --ours  path   # keep our version (rebase source)
git checkout --theirs path  # keep their version (rebase target)
git add path
```

* **需要删除文件（例如 `DU` / 删除与修改冲突）**：

```shell
git rm -- path
# if the file is already gone locally:
git rm --cached -- path
git add -u
```

### 2. 完成变基或合并

```shell
git rebase --continue   # repeat until it finishes
git push origin branch2
```

或
```shell
git commit -m "merge branch1 into branch2"
git push origin branch2
```

<br/>


### 未合并状态码

* `DD` 双方都删除
* `AU` 我方添加
* `UD` 对方删除
* `UA` 对方添加
* `DU` 我方删除 *（通常需决定保留还是删除；使用 `git rm` 删除）*
* `AA` 双方都添加
* `UU` 双方都修改

<br/>


## 历史

### 显示特定文件的提交及差异

```shell
git log -p -- path/to/file
```

### 紧凑的单行历史
```shell
git log --follow --date=short --pretty=format:"%h %ad %an %s" -- path/to/file
```

### 从仓库中移除所有历史：

```shell
	git checkout --orphan new-main
	git add -A
	git commit -m 'new files'
	git branch -D main
	git branch -m main
	git push -f origin main
	git branch --set-upstream-to=origin/main main
```

<br/>

## 还原或撤销最后一次提交

“撤销”最后一次提交有两种截然不同的方式。请根据提交是否已推送来选择。

#### 已推送 → `git revert`（安全，保留历史）

`git revert` 不会删除提交，而是创建一个**新**提交，撤销原提交的更改。历史
得以保留，也无需强制推送，因此适合共享分支或已推送的分支。

```shell
git revert HEAD          # opens an editor for the revert message
git revert --no-edit HEAD   # reuse the default message, no editor
git push
```

若要撤销还原操作本身，只需再次还原（`git revert HEAD`）——或者在还原提交尚未推送时，使用
下面的重置命令将其移除。

#### 仅本地 → `git reset`（重写历史）

如果提交**尚未**推送，将分支指针向后移动一个提交。更改如何处理
取决于所用的选项：

```shell
git reset --soft  HEAD~1   # undo the commit, keep changes staged
git reset --mixed HEAD~1   # undo the commit, keep changes in the working tree (default)
git reset --hard  HEAD~1   # undo the commit AND discard the changes
```

> ⚠️ `--hard` 会永久丢弃该提交在工作树中的更改。请先运行 `git status`（如果
> 不确定，再运行 `git stash`）。

常见情形：保留更改，但重新提交——执行 `git reset --soft HEAD~1`，然后按需重新暂存/提交。

无需重置，也可以只修改提交信息或向最后一次提交补上遗漏的文件：

```shell
git commit --amend            # edit message and/or fold in staged changes
git commit --amend --no-edit  # keep the message, just add the staged changes
```

#### 如果提交已经推送

重置已推送的提交会重写历史，因此推送属于非快进更新，必须强制执行。优先使用
`--force-with-lease`；如果其间有其他人推送，该选项会拒绝此次推送：

```shell
git reset --hard HEAD~1
git push --force-with-lease
```

> ⚠️ 仅在你掌控的分支上这样做。重写共享历史会破坏其他克隆——在共享分支上
> 请改用 `git revert`。

#### 恢复误删的提交

`reset` 不会立即删除提交；原来的分支顶端会在引用日志（reflog）中保留一段时间：

```shell
git reflog                 # find the SHA of the lost commit
git reset --hard <sha>     # or: git cherry-pick <sha>
```

<br/>

## 令牌（个人访问令牌）

**个人访问令牌（PAT）**是绑定到**你的个人账户**的凭据，而非绑定到某个仓库。
始终在以下位置创建：

```
Personal Settings > Developer Settings > Personal access tokens
```

两个容易弄错的关键事实：

* 令牌**继承创建它的账户的权限**。要对某个仓库进行操作（触发其
  工作流、推送、拉取私有镜像），该账户必须对**该**仓库拥有相应的访问权限。
* GitHub **仅在创建时**显示令牌字符串一次。之后无法再次查看（无论是在
  账户设置中，还是在保存了该令牌的机密中）。如果丢失，请重新生成。

你可以通过 `regenerate` 重新生成已有令牌（得到新值），或直接编辑经典令牌的权限范围（值
不变）——两者都在同一页面操作。请始终设置自定义过期日期。

### 我需要哪种权限范围 / 权限？

按令牌必须**执行的操作**选择对应的行，而不是按存放令牌的仓库选择：

| 目标                                      | 经典令牌权限范围        | 细粒度权限                     |
|-------------------------------------------|------------------------|--------------------------------|
| **触发**另一个仓库的工作流（API）         | `repo` / `public_repo` | **Actions → 读写**            |
| 添加 / 编辑 `.github/workflows/*` 文件    | `workflow`             | **Workflows → 读写**          |
| 拉取私有容器镜像                          | `read:packages`        | **Packages → 读取**           |

> ⚠️ 常见错误：`workflow` 权限范围**仅**用于提交工作流文件，**不**允许
> 你*触发*运行。要触发 `workflow_dispatch` / `repository_dispatch`，经典令牌需要 `repo`
> （公开仓库使用 `public_repo`）权限范围，细粒度令牌则需要 **Actions：读写**
> 权限。

### 直接链接

* 细粒度：<https://github.com/settings/personal-access-tokens/new>
  → 所有者选 `gemc`，仓库例如 `gemc/clas12-systems`，权限选 **Actions：读写**
* 经典：<https://github.com/settings/tokens/new>
  → 权限范围：✅ `repo`（涵盖 `public_repo`）；若需拉取私有镜像，添加 `read:packages`

供本地工具（而非工作流）使用的令牌应保存在该工具读取的文件中，通常位于用户主目录，
例如 `.bob`。


<br/>

## 机密

**GitHub Actions 机密（secret）**是存储在仓库设置中的加密变量。该仓库中的
工作流在运行时通过 {% raw %}`${{ secrets.SECRET_NAME }}`{% endraw %} 读取它；其值不会打印到日志中，也不会
向浏览仓库的任何人显示。

区分以下两部分——它们存放在不同的位置：

* **令牌**（即 `ghp_…` / `github_pat_…` 字符串）在**你的个人账户**中创建（见上文）。
* **机密**是该字符串的一个*副本*，存储在**使用它的工作流所属的仓库**中——即
  发起触发的仓库，**而非**被触发的仓库。

### 如何创建并存储

1. 在**你的个人账户**中（Developer settings）**生成令牌**，为希望工作流操作的
   **目标**仓库选择相应的权限范围/权限（见上表）。该账户必须
   对目标仓库拥有写权限。

2. **复制屏幕上显示的令牌值**（仅显示一次）。

3. **将机密添加到使用它的工作流所属的仓库**
   - 进入该仓库 → **Settings → Secrets and variables → Actions**
     （例如 <https://github.com/gemc/pygemc/settings/secrets/actions>）
   - 点击 **New repository secret**
   - 名称：例如 `GEMC_SRC_PAT`（必须与工作流 YAML 中引用的名称一致）
   - 值：粘贴令牌
   - 点击 **Add secret**


<br/>

## 触发另一个仓库中的工作流

内置的 `GITHUB_TOKEN` **无法**启动其他仓库中的工作流，因此跨仓库触发
使用存储为机密的 PAT。其模式是：**仓库 A** 的工作流调用 GitHub API 来触发**仓库
B** 的工作流。

你需要三样东西：

1. **一个 PAT**，所属账户对**仓库 B 拥有写权限**，并且令牌具备触发 Actions 的权限
   （经典令牌的 `repo`，或细粒度令牌对 B 的 **Actions：读写**权限）。见上面的令牌表格。
2. **保存该 PAT 的机密**，存储在**仓库 A**（触发源）中。
3. **仓库 B 的工作流中配置了可通过 API 调用的触发器**——在目标工作流的 `on:` 块中添加 `workflow_dispatch:`
   （可包含可选的 `inputs:`），否则 API 调用会返回 `404`/`422`。

### 触发调用（在仓库 A 的工作流中）

{% raw %}
```yaml
      - name: Trigger workflow_dispatch on repo B
        run: |
          curl --fail-with-body -X POST \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer ${{ secrets.B_PAT }}" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            https://api.github.com/repos/<owner>/<repoB>/actions/workflows/test.yml/dispatches \
            -d '{"ref":"main","inputs":{"triggered_by":"repo A"}}'
```
{% endraw %}

`inputs` 中的键必须与仓库 B 工作流中 `workflow_dispatch:` 下声明的 `inputs:` 相匹配。

### 安全性：为 `workflow_run` 链式触发设置保护条件

使用 `on: workflow_run` 的工作流以**特权**运行（可访问机密/PAT），而且来自 fork 的 PR
事件也能触发它，因此必须为作业设置运行条件——否则，来自 fork 的 PR 可能进入特权步骤，
使通过 `workflow_run.head_sha` 检出的代码在特权上下文中运行。这也是 CodeQL 会标记
“在特权上下文中检出不受信任代码”的原因。

**应检查哪个字段取决于其在触发链中的位置**——这一点很容易出错：

* **第 1 跳**——监听*直接*由 `push`/`pull_request` 触发的工作流（例如 `Deploy`
  通过 `on: workflow_run` 监听 `Test`）：`github.event.workflow_run.event` 是原始事件，因此
  使用 `event == 'push'` 作为保护条件。

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.event == 'push'
        }}
  ```
  {% endraw %}

* **第 2 跳**——监听*本身*由 `workflow_run` 触发的工作流（例如在 `Deploy`
  之后运行的作业，而 `Deploy` 已通过 `on: workflow_run` 触发）：此时 `workflow_run.event` **始终为
  `workflow_run`**，绝不会是 `push`。使用 `event == 'push'` 会让作业永远不运行；使用
  `event == 'workflow_run'` 则始终通过（起不到保护作用）。应改为检查
  源仓库——`head_*` 字段会沿触发链保留原始来源：

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.head_repository.full_name == github.repository
        }}
  ```
  {% endraw %}

  `head_repository.full_name == github.repository` 对于同一仓库的推送为真，对于来自 fork 的 PR
  触发链为假，这正是所需的防止检出不受信任代码的保护条件。

### 本项目中的示例

| 触发源（仓库 A）        | 机密名称（在 A 中）    | 目标（仓库 B）        | 令牌所需权限（对 B）    |
|-------------------------|-----------------------|----------------------|-------------------------|
| `gemc/pygemc`           | `GEMC_SRC_PAT`        | `gemc/src`           | 触发 src 中的 Actions  |
| `gemc/src`              | `CLAS12_SYSTEMS_PAT`  | `gemc/clas12-systems`| 触发 clas12-systems 中的 Actions |
