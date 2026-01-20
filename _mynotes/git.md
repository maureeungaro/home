---
layout: default
title: "Using Git"
---

{% include mynotes.html %}


# Using Git
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


- Clone one branch or tag, w/o history, with submodules w/o their history (shallow)

	```shell
	git clone -b v1.2.3 --recurse-submodules --shallow-submodules --depth 1 [repo] 
	```

<br/>

# Update a tag / release

Use variables to point to the GitHub tag you want to update, the temp branch and the tag ref
For example `5.12` or `v5.12`:

```shell
tag=v1.2.3
btag="b$tag"
ttag="refs/tags/$tag"
```

- Create and switch to a temporary branch (**b**) from the current tag (**t**)

	```shell
	git fetch origin --tags
	git switch -c "$btag" "$tag"
	```

- Make changes, commit and push

	```shell
	git commit -am "Fixes for $tag"
	git push -u origin "$btag"
	```

- Delete old local tag, recreate tag at HEAD

	```shell
	git switch "$btag"
	git tag -d "$tag"        
	git tag "$tag"            
	```

- Delete old remote tag, push the new tag
 
	```shell
	git push origin :"$ttag"
	push origin tag "$tag"
	```

- Update the GitHub release: delete and create new one using new tag

- Cleanup: delete remote temp branch, local temp branch

	```shell
	git push origin --delete "$btag"
	git branch -D "$btag"
	```

<br/>

# Branches

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

If conflicts arises:

1. Open each conflicted file `(<<<<<<<, =======, >>>>>>> markers)`.
2. Manually resolve the conflicts by editing the file.
3. After resolving conflicts, mark the files as resolved:
```shell
git add conflicted_file
```

If necessary, keep one version of the other of one file:

```shell
git checkout --ours conflicted_file  # Keep our version (the rebase source)
git checkout --theirs conflicted_file  # Keep their version (the rebase target)
```

After choosing one version, you still need to `git add` the file to mark it as resolved.

```shell
git add conflicted_file
```

Finalizing rebase (notice commit w/o message):
```shell
git rebase --continue
git push origin branch2
```

The status can be:

- `DD` unmerged, both deleted
- `AU` unmerged, added by us
- `UD` unmerged, deleted by them
- `UA` unmerged, added by them
- `DU` unmerged, deleted by us
- `AA` unmerged, both added
- `UU` unmerged, both modified



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


# History

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

# Tokens

Can use 'regenerate' to copy the configuration

Configuration:

repo --> public_repo 

For private images, the token must have at least read:packages.
