---
aliases: []
author: Maneesh Sutar
created: 2024-04-05
modified: 2025-04-14
tags: []
title: Poetry
---

# Poetry

Poetry is a tool for **dependency management** and **packaging** in Python  
Alternative to setuptools

## Installation

 > 
 > Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system

### Official Installer

[Official installer](https://python-poetry.org/docs/#installing-with-the-official-installer) (recommended) with curl can work on all devices:

`curl -sSL https://install.python-poetry.org | python3 -`

See advanced section in [Official installer](https://python-poetry.org/docs/#installing-with-the-official-installer) for configuration option  
This has no depedencies on any other thing. But it stores all the binaries (including python), might take larger space

### With pipx

[pipx](https://pipx.pypa.io/stable/) installs packages in their own isolated virtual envrironment, typically under ~/.local/pipx/envs .  
pipx itself depends upon a python interpreter, so it will use (symlink) one of the python installed in system.  
Poetry installed from pipx will “try” to reuse (i.e. if version is supported) the already existing python, thus reducing the space taken. BUT site-packages will be kept seprately from the parent python.

````bash
# on mac
brew install pipx # will use python from brew's installed python
# on linux
pip install pipx # pipx will use the python corresponding to pip

pipx install poetry # will re-use pipx's python
````

## Basic usage

`pyproject.toml` file in your python project will contain all the configuration regarding poetry.  
[Link to doc](https://python-poetry.org/docs/pyproject/) on the config inside toml file

## Poetry configuration

Poetry (itself) can be configured via the `poetry config` command ([see more about its usage here](https://python-poetry.org/docs/cli/#config "config command documentation"))  
The config can be global or local (`--local`) to the project  
Global config file is typicall present under `~/.config/pypoetry`. See [default directories](https://python-poetry.org/docs/configuration/#default-directories)  
See [config doc](https://python-poetry.org/docs/configuration/).

## Virtualenv

See [poetry env doc](https://python-poetry.org/docs/managing-environments/).  
By default, **for every new project, Poetry creates a virtual environment** in `{cache-dir}/virtualenvs`.  
You can turn off this behaviour, although I feel having different environements per project is a plus.  
The poetry config `virtualenvs.in-project` can be set to true to create virtual environments within your project directory.  
The `poetry env` command can be used to modify the environment of the current project

## Managing project with Poetry

To create a new project managed with poetry : `poetry new project-dir-name`  
Above command will create a template project structure with default `pyproject.toml` file.

To manage existing project

````bash
cd pre-existing-project
poetry init
````

`poetry init` This will start an interactive cli where you can specify all the main configs, add dependencies etc. Finally it will generate `pyproject.toml` file

## Depedency management

Main doc: <https://python-poetry.org/docs/dependency-specification/>

To add a new dependency to the project: `poetry add <dependency>`  
By default it will search the dependency in `pypi` , and ask user to choose the correct package and version interatively. Then it will update `pyproject.toml`  
Once added, it will also install the dependency in the poetry's [virtual environment](#virtualenv)

The dependencies can be of type pipy packages, git urls, web urls, local paths, or even tarballs.  
For **versioning**, there are different constraints which one can apply for dependencies, such as Caret, Tilde etc. each with a specific rule.

In the `pyproject.toml` file  
`[tool.poetry.dependencies]`  specify the project's cumpulsory dependencies  
`[tool.poetry.extras]` specify the "extra" dependencies, similar to setuptools **extras_require**  
Please refer <https://python-poetry.org/docs/pyproject/#extras> for more info on extras

## Enabling CLI scripts for the project

Poetry can build your project to be run as a CLI application

Read more: <https://python-poetry.org/docs/pyproject/#scripts>

## Dependency groups

Poetry provides a way to **organize** your dependencies by **groups**.  
To declare a new dependency group, use a `tool.poetry.group.<group>` section where `<group>` is the name of your dependency group (for instance, `test`):  
When adding a new dependency, we can use `poetry add --group <group> <dependencies>` to specify the group

**Things to note:**

1. Dependencies listed in [dependency groups](https://python-poetry.org/docs/managing-dependencies/#dependency-groups) **cannot be specified** as **extras** (as in setuptools **extras_require**). [Extras](https://python-poetry.org/docs/pyproject/#extras) is different.

1. All dependencies **must be compatible with each other across groups** since they will be resolved regardless of whether they are required for installation or not (see [Installing group dependencies](https://python-poetry.org/docs/managing-dependencies/#installing-group-dependencies)).

1. The default set of dependencies for a project includes the **implicit** `main` **group** defined in `tool.poetry.dependencies` as well as all groups that are not explicitly marked as an [optional group](https://python-poetry.org/docs/managing-dependencies/#optional-groups).

1. **By default**, dependencies across **all non-optional groups** will be installed when executing `poetry install`. The options `--with` , `--without` and `--only` can be used to specify particular groups to be installed/not-installed

1. Installing dependencies present in non- `main` groups **is only possible by using Poetry** i.e. with the `pyproject.toml` file. They are not exported when packaging. **Treat them as development dependencies.**

## Synchronising Deps with .lock file

Poetry supports what’s called dependency synchronization.  
Dependency synchronization ensures that the locked dependencies in the `poetry.lock` file are the only ones present in the environment, **removing anything that’s not necessary**.

This is done by using the `--sync` option of the `install` command:

````bash
poetry install --sync
````
