---
layout: default
title: "Using Git"
---

{% include mynotes.html %}


# Using Git
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## Clone one branch or tag, w/o history, with submodules w/o their history (shallow)

```shell
git clone -b v1.2.3 --recurse-submodules --shallow-submodules --depth 1 [repo] 
```

<br/>

## Update a tag / release (rewrite an existing tag)

**Use these Variables**

* `tag`: the GitHub tag name (e.g. `v1.2.3`)
* `btag`: temporary branch name created from the tag
* `rtag`: full tag ref path (`refs/tags/<tag>`), used for remote deletion

Example:

```sh
tag=v1.2.3
btag="b$tag"
rtag="refs/tags/$tag"
```

#### 1) Create and switch to a temporary branch from the existing tag

```sh
git fetch origin --tags
git switch -c "$btag" "$tag"
```

#### 2) Make changes, commit, and push the temporary branch

```sh
git commit -am "Fixes for $tag"
git push -u origin "$btag"
```

#### 3) Delete old local tag, recreate the tag locally at the new HEAD

(You’re already on `$btag`, so the extra `git switch "$btag"` is redundant.)

```sh
git tag -d "$tag"
git tag "$tag"
```

#### 4) Replace the remote tag

First delete the old remote tag, then push the new one. 
Force-update the remote tag explicitly because tags are immutable by convention and many servers reject non-fast-forward tag updates unless forced.

```sh
git push origin ":$rtag"
git push --force origin "$rtag"
```

#### 5) Update the GitHub release

* Delete the existing release for `$tag`
* Create a new release pointing at the updated `$tag`


#### 6) Cleanup: delete the temporary branch (remote + local)

```sh
git push origin --delete "$btag"
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

## Conflicts

- Check what’s conflicted:

```sh
git status
```

- Resolve each conflicted path, then stage it to mark resolved:

* **Text conflicts (`UU`, etc.)**: open file and fix `<<<<<<< ======= >>>>>>>`, then:

```sh
git add path
```

* **Keep one side** (still requires `git add`):

```sh
git checkout --ours  path   # keep our version (rebase source)
git checkout --theirs path  # keep their version (rebase target)
git add path
```

* **You want the file removed (e.g. `DU` / delete-vs-modify conflict)**:

```sh
git rm -- path
# if the file is already gone locally:
git rm --cached -- path
git add -u
```


- Finalize a rebase

```sh
git rebase --continue   # repeat until it finishes
git push origin branch2
```

- Finalize a merge (non-rebase)

```sh
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

To remove all history from a repo:

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

## Tokens

Can use 'regenerate' to copy the configuration

Configuration:

repo --> public_repo 

For private images, the token must have at least read:packages.
