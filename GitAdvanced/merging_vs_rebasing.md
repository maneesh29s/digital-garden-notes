---
aliases: []
author: Maneesh Sutar
date: 2024-01-19
tags:
- git
title: Merge vs Rebasing
---

# Merge vs Rebasing

<https://www.atlassian.com/git/tutorials/merging-vs-rebasing>

|Merge|Rebase|
|-----|------|
|Merge (by default, most of the time) will create either a new commit merge using ort/octopus strategy|Rebase will never make a new commit. In case of conflict, **the rebase will by default amend the resolved conflicts into the last commit**|
|When possible, merge can fast-forward a commit ( only update the branch pointer to match the merged branch; do not create a merge commit )||
|Merge is safe, as it never alters the commit history|Rebasing always changes the history of the current branch, for the commits which are being moved|
|Multiple merges from main branch to feature branch can make the history of feature branch look ugly|Rebasing helps in keeping a linear history of the branch|

## Good practices

### Merge

1. Use merge when you **don't want to alter the history**. Safest option!
1. To be safe, use `git merge --no-commit --no-ff <feature>`. Option `no-commit` allows developer to look at the changes being added into the merge commit. Option `no-ff` not fast-forward the main even if its possible, creating a merge commit instead.
1. A fast forwarded merge is similar to a rebase. **A fast-forwarded merge will also add the whole commit history from feature branch** on top of main branch. This will lengthen the main's commit history, and we won't be able to track exactly when the commits from feature were merged into the main.
1. If you **don't wish your feature branch commit history to be part of the main branch**, run `git merge --squash <feature>`. This squashes the changes in all the commits of the feature, adding them to the "working/staged area". This allows you to create a single (regular) commit (not a merge commit) on top of the main whose effect is the same as merging another branch.

### Rebase

 > 
 > Changes the base of your branch

1. Rebase is **history altering**, which will cause local and remote repos to diverge. So key rule is to **never rebase on public branches**
1. Use **rebase on private branches only**, as it helps to keep your history clean.
1. Rebasing a feature on main before creating a pull request to main can help in **no-conflict fast-forwarded** merge with the main.
1. Use `git rebase -i <source>` for **interactive rebasing**. The source can either be
1. Another branch (like main)
1. A previous commit in the feature itself (HEAD~3: 3 commits behind head)  
   You can select which commit to "pick" or "fixup", and you can reorder the commits to make the history look like however you want.  
   The `git merge-base feature main` command returns the **commit-id of the original base** of the `feature` branch (i.e. when it was branched out from main)
