---
layout: default
title: "Using Git"
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Using Git
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## Clone one branch or tag, w/o history, with submodules w/o their history (shallow)

```shell
git clone -b v1.2.3 --recurse-submodules --shallow-submodules --depth 1 [repo] 
```

<br/>

## Git LFS (Large File Storage)

Install Git LFS, then initialize it once for your user account:

```shell
# macOS
brew install git-lfs

# Ubuntu/Debian
sudo apt install git-lfs

git lfs install
```

Enable Git LFS in a repository and select the file types to store with it:

```shell
cd path/to/repository
git lfs track "*.zip"       # use a pattern or a specific file path
git add .gitattributes      # commit the tracking rules
git add path/to/archive.zip
git commit -m "Track ZIP files with Git LFS"
git push
```

Run `git lfs ls-files` to list tracked files. Tracking a pattern affects newly added files only; moving files
already committed to regular Git into LFS requires `git lfs migrate`, which rewrites repository history.

<br/>

## Publish an immutable release and move its major-version tag

Use two tags for a versioned GitHub Action or other project:

* `v1.0.1` is the immutable release tag. Never move or reuse it.
* `v1` is a moving compatibility tag. Users who specify `uses: owner/repository@v1` receive the latest
  compatible `v1.x.x` release.

The GitHub Release must remain attached to `v1.0.1`. Only the `v1` tag moves; there is no separate moving
GitHub Release.

#### 1) Publish the GitHub Release

On the repository's GitHub page:

1. Open **Releases** and select **Draft a new release**.
2. Create (or choose) the `v1.0.1` tag. 
3. Add the release title, notes, and any assets.


#### 2) Create or update the major-version tag

Set the immutable version and the moving major version:

```shell
version=v1.0.1
major=v1
```

Only after the GitHub Release for `v1.0.1` is published, point `v1` at it. On the first release this creates
`v1`; on every later release (`v1.0.2`, `v1.1.2`, ...) the same command updates `v1` to the newest immutable
tag. Fetch the tag GitHub just created, point the local `v1` tag at the commit referenced by `$version`, then
force-update only that tag on GitHub:

```shell
git fetch origin tag "$version"
git tag -f "$major" "$version^{}"
git push --force origin "refs/tags/$major"
```

The `^{}` suffix dereferences the version tag, so `v1` points directly to the release commit. Force is
required because moving a tag is a non-fast-forward update (and is harmless the first time, when `v1` does not
yet exist). Protect immutable tags such as `v*.*.*` with a GitHub tag ruleset, while allowing the major tags
intended to move.

<br/>

## Update a tag / release (rewrite an existing tag)

**Use these Variables**

* `tag`: the GitHub tag name (e.g. `v1.2.3`)
* `btag`: temporary branch name created from the tag
* `rtag`: full tag ref path (`refs/tags/<tag>`), used for remote deletion

Example: `tag=v1.2.3`

```shell
btag="b$tag"
rtag="refs/tags/$tag"
```

#### 1) Create and switch to a temporary branch from the existing tag

```shell
git fetch origin --tags
git switch -c "$btag" "$tag"
```

#### 2) Make changes, commit, and push the temporary branch

```shell
git commit -am "Fixes for $tag"
git push -u origin "$btag"
```

#### 3) Delete old local tag pointing to the old commit, recreate the tag locally at the new HEAD

(You’re already on `$btag`, so the extra `git switch "$btag"` is redundant.)

```shell
git tag -d "$tag"
git tag "$tag"
```

#### 4) Replace the remote tag pointing to the new commit

First delete the old remote tag, then push the new one. 
Force-update the remote tag explicitly because tags are immutable by convention and many servers reject non-fast-forward tag updates unless forced.

```shell
git push origin ":$rtag"
git push --force origin "$rtag"
```

#### 5) Update the GitHub Release (and assets) if necessary
* If you uploaded release assets (binaries / custom .tar.gz / etc.):
   update the existing release by removing the old assets and uploading the new ones (or delete and recreate the release).
   Moving the tag does not replace uploaded assets.
* If only GitHub-generated source archives are used (“Source code (tar.gz/zip)”):
  you can usually leave the release as-is; it will continue to be “for $tag”, and the generated archives will 
  follow the updated tag (may take a short while due to caching).
* If release notes/changelog should change:
  either edit the existing release notes, or delete and recreate the release for $tag.

#### 6) Cleanup: delete the temporary branch (remote + local)

```shell
git push origin --delete "$btag"
git switch main
git branch -D "$btag"
```


<br/>

## Branches

Create new branch and switch to it:

```shell
git checkout -b branchname
```

Switch to an existing branch:

```shell
git checkout branchname
```

Merge changes from branch1 into branch2 (one of them can be main). Use `rebase` for a clean history. 
Alternatively, you can use `merge` to keep the history of both branches.
```shell
git checkout branch2
git merge/rebase branch1 
```

Push a branch to remote:

```shell
git push -u origin branchname
```

Delete a remote branch:

```shell
git push origin --delete branchname
```

List all remote branches:

- `git branch -r`: lists all remote branches
- `git branch -a`: lists all branches (local and remote)
- `git branch -vv`: lists all branches with their last commit
- `git branch --merged`: lists branches that have been merged into the current branch
- `git branch --no-merged`: lists branches that have not been merged into the current branch


<br/>

## Take specific files from another branch (not a full merge)

When you only want one or a few files from another branch (or commit/tag), don't merge the whole branch —
pull just those paths into your current working tree.

> ⚠️ These commands **overwrite** the local copy of the listed paths. Any uncommitted changes to them are
> lost. Run `git status` first if unsure.

#### Preview the difference first

```shell
git diff main..otherbranch -- path/to/file        # what would change in that file
git show otherbranch:path/to/file                 # print the file as it is on otherbranch
```

#### Copy the files over (replace local version)

```shell
# Modern (recommended). --source can be a branch, tag, or commit SHA.
git restore --source=otherbranch --staged --worktree -- path/to/file [more/files...]

# Classic equivalent (also stages the result):
git checkout otherbranch -- path/to/file [more/files...]
```

`git checkout <branch> -- <path>` updates both the working tree and the index (already staged).
`git restore --source=<ref> -- <path>` updates only the working tree by default — add `--staged` (as above)
to also stage it. Then commit normally:

```shell
git add path/to/file        # only needed if the file is not already staged
git commit -m "Bring path/to/file from otherbranch"
```

#### Take only some changes within a file (interactive, hunk by hunk)

This is the closest thing to "merging" a single file: pick which hunks to bring in.

```shell
git restore -p --source=otherbranch -- path/to/file   # or: git checkout -p otherbranch -- path/to/file
```

#### True 3-way merge of a single file

`checkout`/`restore` *replace* the file; they do not merge its content with yours. For an actual
line-by-line merge of one file between two versions, use `git merge-file`:

```shell
git show otherbranch:path/to/file > /tmp/theirs       # their version
git show $(git merge-base HEAD otherbranch):path/to/file > /tmp/base   # common ancestor
git merge-file path/to/file /tmp/base /tmp/theirs     # merges into path/to/file, marks conflicts
```


<br/>

## Conflicts

### 1. Resolve Conflicts

- Check what’s conflicted:

```shell
git status
```

* **Text conflicts (`UU`, etc.)**: open file and fix `<<<<<<< ======= >>>>>>>`, then:

```shell
git add path
```

* **Keep one side** (choose ours or theirs):

```shell
git checkout --ours  path   # keep our version (rebase source)
git checkout --theirs path  # keep their version (rebase target)
git add path
```

* **You want the file removed (e.g. `DU` / delete-vs-modify conflict)**:

```shell
git rm -- path
# if the file is already gone locally:
git rm --cached -- path
git add -u
```

### 2. Finalize a rebase or a merge

```shell
git rebase --continue   # repeat until it finishes
git push origin branch2
```

or
```shell
git commit -m "merge branch1 into branch2"
git push origin branch2
```

<br/>


### Unmerged status codes

* `DD` both deleted
* `AU` added by us
* `UD` deleted by them
* `UA` added by them
* `DU` deleted by us *(often: decide keep vs delete; use `git rm` to delete)*
* `AA` both added
* `UU` both modified

<br/>


## History

### Show commit + diff for a specific file

```shell
git log -p -- path/to/file
```

### Compact one-line history
```shell
git log --follow --date=short --pretty=format:"%h %ad %an %s" -- path/to/file
```

### To remove all history from a repo:

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

## Tokens (Personal Access Tokens)

A **Personal Access Token (PAT)** is a credential tied to **your personal account**, not to a repository.
You always create it under:

```
Personal Settings > Developer Settings > Personal access tokens
```

Two key facts that are easy to get wrong:

* The token **inherits the permissions of the account that creates it**. To act on a repo (trigger its
  workflows, push, pull private images), that account must have the matching access to **that** repo.
* GitHub shows the token string **only once**, at creation. It cannot be read back later (not from your
  settings, not from a secret it was pasted into). If you lose it, regenerate.

You can `regenerate` an existing token (new value) or edit a classic token's scopes in place (value
unchanged) — both under the same page. Always set a custom expiration date.

### Which scope / permission do I need?

Pick the row for what the token must **do**, not for the repo it lives in:

| Goal                                      | Classic scope          | Fine-grained permission        |
|-------------------------------------------|------------------------|--------------------------------|
| **Trigger** another repo's workflow (API) | `repo` / `public_repo` | **Actions → Read and write**   |
| Add / edit `.github/workflows/*` files    | `workflow`             | **Workflows → Read and write** |
| Pull private container images             | `read:packages`        | **Packages → Read**            |

> ⚠️ Common mistake: the `workflow` scope is **only** for committing workflow files. It does **not** let
> you *trigger* a run. To fire a `workflow_dispatch` / `repository_dispatch` you need `repo`
> (`public_repo` for public repos) on a classic token, or **Actions: Read and write** on a fine-grained
> token.

### Direct links

* Fine-grained: <https://github.com/settings/personal-access-tokens/new>
  → Owner `gemc`, repo e.g. `gemc/clas12-systems`, permission **Actions: Read and write**
* Classic: <https://github.com/settings/tokens/new>
  → Scope: ✅ `repo` (covers `public_repo`); add `read:packages` for private images

A token used by a local tool (not a workflow) should go in a file read by that tool, typically in the home
dir, for example `.bob`.


<br/>

## Secrets

A **GitHub Actions secret** is an encrypted variable stored in a repository's settings. Workflows in that
repository read it at runtime via {% raw %}`${{ secrets.SECRET_NAME }}`{% endraw %}; the value is never printed in logs or
shown to anyone browsing the repo.

Keep the two pieces separate — they live in different places:

* **The token** (the `ghp_…` / `github_pat_…` string) is created in **your personal account** (above).
* **The secret** is a *copy* of that string, stored in the repository **whose workflow will use it** — i.e.
  the repo that does the triggering, **not** the repo being triggered.

### How to create and store it

1. **Generate the token** in your **personal account** (Developer settings), choosing the scope/permission
   for the **target** repo you want the workflow to act on (see the table above). The account must have
   write access to that target repo.

2. **Copy the token value** shown on screen (visible only once).

3. **Add the secret to the repository whose workflow uses it**
   - Go to that repo → **Settings → Secrets and variables → Actions**
     (e.g. <https://github.com/gemc/pygemc/settings/secrets/actions>)
   - Click **New repository secret**
   - Name: e.g. `GEMC_SRC_PAT` (must match the name referenced in the workflow YAML)
   - Value: paste the token
   - Click **Add secret**


<br/>

## Triggering a workflow in another repository

The built-in `GITHUB_TOKEN` **cannot** start workflows in a different repository, so cross-repo triggers
use a PAT stored as a secret. The pattern: **repo A**'s workflow calls the GitHub API to dispatch **repo
B**'s workflow.

You need three things:

1. **A PAT** owned by an account with **write access to repo B**, scoped to trigger Actions
   (classic `repo`, or fine-grained **Actions: Read and write** on B). See the Tokens table above.
2. **The secret** holding that PAT, stored in **repo A** (the trigger source).
3. **A dispatchable trigger on repo B's workflow** — add `workflow_dispatch:` (with optional `inputs:`) to
   the `on:` block of the target workflow, otherwise the API call returns `404`/`422`.

### The dispatch call (in repo A's workflow)

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

The `inputs` keys must match the `inputs:` declared under `workflow_dispatch:` in repo B's workflow.

### Security: guard `workflow_run`-chained triggers

A workflow with `on: workflow_run` runs **privileged** (it can see secrets/PATs) and fires for fork-PR
events too, so gate the job — otherwise a fork PR could reach the privileged step and any code it checks
out via `workflow_run.head_sha`. This is also why CodeQL flags "checkout of untrusted code in a privileged
context".

**Which field to check depends on the position in the chain** — this trips people up:

* **1st hop** — listening to a workflow triggered *directly* by `push`/`pull_request` (e.g. a `Deploy`
  that runs `on: workflow_run` of `Test`): `github.event.workflow_run.event` is the original event, so
  guard with `event == 'push'`.

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.event == 'push'
        }}
  ```
  {% endraw %}

* **2nd hop** — listening to a workflow that is *itself* `workflow_run`-triggered (e.g. a job that runs
  after `Deploy`, which already runs `on: workflow_run`): here `workflow_run.event` is **always
  `workflow_run`**, never `push`. Using `event == 'push'` makes the job never run; using
  `event == 'workflow_run'` always passes (no protection). Guard on the source repo instead — the
  `head_*` fields carry the original source through the chain:

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.head_repository.full_name == github.repository
        }}
  ```
  {% endraw %}

  `head_repository.full_name == github.repository` is true for same-repo pushes and false for fork-PR
  chains, which is exactly the untrusted-code-checkout protection you want.

### Examples in this project

| Trigger source (repo A) | Secret name (in A)    | Target (repo B)      | Token needs (on B)      |
|-------------------------|-----------------------|----------------------|-------------------------|
| `gemc/pygemc`           | `GEMC_SRC_PAT`        | `gemc/src`           | trigger Actions on src  |
| `gemc/src`              | `CLAS12_SYSTEMS_PAT`  | `gemc/clas12-systems`| trigger Actions on clas12-systems |
