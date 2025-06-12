---
layout: default
title: "Using Git"
---

{% include mynotes.html %}

---

<br/>


# Branches

Create new branch and switch to it:

```bash
git checkout -b branchname
```

Switch to an existing branch:

```bash
git checkout branchname
```

Merge changes from branch1 into branch2 (one of them can be main). Use `rebase` for a clean history. 
Alternatively, you can use `merge` to keep the history of both branches.
```bash
git checkout branch2
git rebase branch1 
```

If conflicts arises:

1. Open each conflicted file `(<<<<<<<, =======, >>>>>>> markers)`.
2. Manually resolve the conflicts by editing the file.
3. After resolving conflicts, mark the files as resolved:
```bash
git add conflicted_file
```

If necessary, keep one version of the other of one file:

```bash
git checkout --ours conflicted_file  # Keep our version
git checkout --theirs conflicted_file  # Keep their version
```


Finalizing rebase (notice commit w/o message):
```bash
git commit
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

```bash
git push -u origin branchname
```

Delete a remote branch:

```bash
git push origin --delete branchname
```


List all remote branches:

- `git branch -r`: lists all remote branches
- `git branch -a`: lists all branches (local and remote)
- `git branch -vv`: lists all branches with their last commit
- `git branch --merged`: lists branches that have been merged into the current branch
- `git branch --no-merged`: lists branches that have not been merged into the current branch
