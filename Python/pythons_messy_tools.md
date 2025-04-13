---
aliases: []
author: Maneesh Sutar
created: 2024-04-04
modified: 2025-04-14
tags: []
title: All the messy tools in python
---

# All the messy tools in python

[Python Packaging Authority](https://github.com/pypa) is the organisation which manages all the core tools supporting python

## Package Managers

Purpose: only manage **python packages** inside a python installation (typically present under lib/site-packages)

Packages are libraries and/or cli application, written in python / depend on python interpreter  
Packages are (typically) installed from a remote repo such as PyPi, Conda

The **[pip](https://github.com/pypa/pip)** is the basic package manager, **installed with every python**, present as executable + python module.  
pip depends on its "parent" python (the one with which it was installed)

pip typically **installs the packages in its parent python's site packages** folder, OR **in the virtual env** it resides in

 > 
 > By default, the "venv" command will create a new binary of "pip" particular to that environment, which will install new packges in that environment itself

**[pipx](https://github.com/pypa/pipx)** is a **python cli** specialized package installer. It can **only be used to install packages with cli entrypoints** in their **isolated envrionments.**  
it lets you install cli applications but NOT libraries that you import in your code.  
pipx relies on its parent python, pip (and venv)

## Virtual Environment Managers

Purpose: python offers **virtual environments to** **isolate packages**, so that your different applications can use different versions of the packages.

[virtualenv](https://github.com/pypa/virtualenv) is the OG python environment manager.  
Since Python `3.3`, a subset of it has been integrated into the standard library under the [venv module](https://docs.python.org/3/library/venv.html). See [doc](https://virtualenv.pypa.io/en/latest/) for differences.  
**virtualenv** is a CLI tool, while **venv** is only available as a python module (need to run as `python -m venv`)

 > 
 > By default,  different virtual envrironments generated from the same virtualenv/venv comand, **will share** the **parent python** executable. The site-packages will not be shared among virtual environments, that's how you get package isolation

## Python Version Managers

Purpose: manage **different versions of the python interpreter** itself.

**[pyenv](https://github.com/pyenv/pyenv)** is a python version manager. pyenv is **not part** of the [Python Packaging Authority](https://github.com/pypa)  
Important thing is **pyenv does not depend on python at all**, its mostly written in shell scripts.  
It also supports virtual environment using a plugin [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).

## And here comes... Conda and Mamba

**Conda: Python Version Manager + Package Manager  + Environment Manager**  
**So use conda, be at ease !**  
at least until the licence is not changed

**mamba** (hosted at [mamba-org/mama](https://github.com/mamba-org/mamba) ) is alternative to conda, written in C, fully compatible with conda packages (at least the one in [conda-forge](https://github.com/conda-forge)).  
Although it started as a wrapper over conda, now some core functionalities are written in C. So **its faster**.  
Main differentiater was faster package dependency resolver using [libsolv](https://github.com/openSUSE/libsolv) (also used in rpm, yum)  
Although in 2023 conda also added [libmamba-solver](https://github.com/conda/conda-libmamba-solver?tab=readme-ov-file)

Anyway, the goal of "mamba-org" is to provide conda-like features while  removing dependency anaconda.com  
They are planning to self-host another repository. See [quetz](https://github.com/mamba-org/quetz). [Learn more](https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23).

Also mamba encourages users to use conda-forge channel, and remove conda's default channel. [Learn more](https://mamba.readthedocs.io/en/latest/user_guide/troubleshooting.html#using-the-defaults-channels)

 > 
 > The [Anaconda default channels](https://docs.anaconda.com/free/anaconda/reference/default-repositories/) are **incompatible** with conda-forge.

The **mamba-org** actually provides has 2 tools,

**mamba** : depends on conda for some features. Similar to conda it has base environment. The installer also has pre-configured .condarc/.mambarc files.  
[conda-forge/Miniforge](https://github.com/conda-forge/miniforge/tree/main) is a **community-driver installer** which installs both **mamba** and **conda**. It **replaces** [Miniconda](https://docs.anaconda.com/free/miniconda/). In this case, both conda and mamba share the base environment, and install packages and create new envs in `~/miniforge3`  folder. Miniforge also sets the [conda-forge](https://github.com/conda-forge)  as the default package repository for both conda and mamba, removing anaconda's default.

**micromamba** :  `micromamba` is a small, pure-C++ reimplementation of `mamba`/`conda`. It **strives to be a full replacement** for `mamba` and `conda`. As such, it doesn't use any `conda` code (in fact it doesn't require Python at all).  
By default it provides a completely empty base environment (unlike conda or mamba which contain their dependencies)  
See the [documentation on `micromamba`](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) for details.

## What to do in future if conda is banned?

Or if conda has some licensing issue.  
Then you can move to these options, from easy to hard

1. Use `micromamba` which is totally independent from conda. The full `mamba` may or may not be useful since it (at least at the time of writing) depends on conda for some features.

1. Use `pyenv` with its virtual env plugin, and inside each enviironment use `pip` to manage packages. Using `pyenv` is preferred since its independent of python.

1. Use your system's package manager (`apt`, `brew`) to install `virtualenv` . Use  `virtualenv` to manage multiple pythons and envrionments, and `pip` for package management.

## Python Development Tools

[setuptools](https://setuptools.pypa.io/en/latest/userguide/) is the OG python packaging tool, **comes by default with every python**. Used in projects to define project dependencies and to build projects. Very less automation, need to mannually write `setup.py` or (the recently standardized) `pyproject.toml` manifest files.

[pipenv](https://github.com/pypa/pipenv): Pipenv automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your `Pipfile`  as you install/uninstall packages. nicely bridges the gaps between pip, python (using system python, pyenv or [asdf](https://github.com/asdf-vm/asdf)) and virtualenv

[poetry](https://python-poetry.org/docs/) : is more or less **pipenv+setuptools** with its own customisations and features. It is not part of the [pypa](https://github.com/pypa).  more on [poetry](poetry.md)

[A good read](https://dev.to/farcellier/i-migrate-to-poetry-in-2023-am-i-right--115) comparing pipenv, setuptools and poetry:
