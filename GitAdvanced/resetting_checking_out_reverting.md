---
aliases: []
author: Maneesh Sutar
created: 2024-02-10
modified: 2024-09-28
tags:
- git
title: Resetting, checking out & reverting
---

# Resetting, checking out & reverting

<https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting>

|Command|Scope|Common use cases|
|-------|-----|----------------|
|`git reset`|Commit-level|Discard commits in a private branch or throw away uncommitted changes|
|`git reset`|File-level|**Unstage** a file|
|`git checkout`|Commit-level|Switch between branches or inspect old snapshots|
|`git checkout`|File-level|Discard changes in the **working directory**|
|`git revert`|Commit-level|Undo commits in a public branch by making a new commit|
|`git revert`|File-level|(N/A)|

## Good Practice

1. Prefer `git reset` when you wish to do some commit level changes, avoid it for file level. Learn the options `--mixed(default), --soft and --hard`.

1. `git reset` can be **history altering.** In such cases,
   
   1. use `git reflog` to fix your mess up.
   1. use `git reset -p` to interactively change the history
1. Prefer `git switch` over `git checkout` for switching between branches or creating new branches

1. Using `git reset` or `git checkout` on a file level might be confusing as we need to know what they do by default. Instead use `git restore`, specifying the `--source=<treeish>` and whether to do changes in `--worktree` (default) or `--staged`
   
   \|Command|Equivalent|  
   \|---|---|  
   \|`git reset HEAD~2 ./readme`\|`git restore --staged --source=HEAD~2 ./readme`\|  
   \|`git checkout HEAD~2 ./readme`\|`git restore [--worktree] --source=HEAD~2 ./readme`\|
   
   Also use patch mode `-p` to make changes interactively

1. But remember both **switch and restore** commands are **experimental** as of git 2.43.1
