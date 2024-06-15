---
aliases: []
author: Maneesh Sutar
date: 2024-03-02
tags:
- public
- git
title: Advanced git log
---

# Advanced git log

Install tldr  
Run `tldr git log`, you will get enough commands

## Formatting output

Graph output: `git log --oneline --decorate --graph`

For diffs: `git log --stat` , `git log -p`

For grouping logs w.r.t authors, `git shortlog`

Custom formatting: `git log --pretty=format:"%cn committed %h on %cd"`

## Filtering history

Limit output to last n commits: `git log -3`

by date: `git log --before="yesterday" --after="2022-7-1"`

by author: `git log --author="james"`

by commit message: `git log --grep "commited"`

by file: `git log -- <filename>`

by content: `git log -S "hello world!"`

show commits between range of refs : `git log HEAD~4..main`

only merge commits / all non-merge commits: `git log --merges / --no-merges`
