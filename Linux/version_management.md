---
aliases: []
author: Maneesh Sutar
date: 2024-03-27
tags:
- public
- linux
title: Package Version management
---

# Package Version management

## modulefiles

Learn more: <https://modules.readthedocs.io/en/latest/INSTALL.html>

1. Use `modulefiles` to manage custom installed libraries. Run `module avail` to see list of available modules. Run `module --help` for more information.

1. `MODULEPATH` variable in your environment will be used by `module` command to search for available modules. Recommended MODULEPATH for a user is `~/Documents/opt/modulefiles`

## conda

Typically get conda from **miniconda**

 > 
 > Also read [Python's messy tools](../Python/pythons_messy_tools.md)

Local Installation: user level, in `$HOME/miniconda3`

Global Installation: Somewhere in `/opt/miniconda3` ,  
needs sudo access, also need to change install location during installation  
The global conda can then be setup individually for each user with a `conda init` something like command  
Then each user can create conda envs in its local `$HOME/.conda` path

### Steps to remove local install conda

Assume miniconda is install in $HOME/miniconda3 for the current user.

1. Backup the current installation directory i.e. ~/miniconda3. This will be handy later if you want to use the same envrionments without reinstalling them. Else at least backup the environments using following command:
   
   ````sh
   mkdir conda-env-yamls && cd conda-env-yamls
   
   conda env list | grep -v '#' | grep -v '^$' |  awk '{print $1}' | while read -r env_name ; do conda env export -n ${env_name} > ${env_name}-env.yaml ; done
   ````

1. Install `anaconda-clean` in the base environment, run `anaconda-clean` to clean up dotfiles. It will show which files will be removed. `anaconda-clean` is supposed to create a backup directory, but in both Ryzen and Intel WS, it did not create a backup dir at home. So do a manual backup first

1. To delete current installation in ~/miniconda3, simply run `rm -r ~/miniconda3`

1. Delete lines regarding "conda initialise" from all your shell dotfiles (.bashrc, .zshrc, any other)

1. Reload the shell (logout and login) to see if you can still access conda (you shouldn't be able to).

### Steps to install conda globally

1. Download the latest miniconda3 installer <https://docs.conda.io/projects/miniconda/en/latest/>. Check shasum.

1. Run installer with sudo.

1. Select installation dir as "/opt/miniconda3".

1. After installation, "DO NOT" initialise the environment via the installation setup.

1. Run `/opt/miniconda3/bin/conda init` to initialise conda in your shell, which will add "conda initialise" section in your dotfiles.

1. Logout and login. Run `conda info` to see details of the installation.

### Steps to get back previous envionments

1. If you backedup previous conda installation dir, say "~/miniconda3" ; and your new dir is "/opt/miniconda3", then to get back the previous envrionments, simply run the command

````sh
cp ~/miniconda3/envs/* /opt/miniconda3/envs/
````

## apt (ubuntu)

### How to manage alternate versions of the same app using OS pkg manager?

For ubuntu, uses `apt` , Using  `update-alternatives`  
It maintains symbolic links determining default commands

The RHEL, which uses dnf/yum package manager, has `alternatives` command to achive the same. [Know more](https://www.redhat.com/sysadmin/alternatives-command)

e.g. To know how to install multiple gcc versions and manage them: <https://phoenixnap.com/kb/install-gcc-ubuntu>

This is how update-alternatives  will create a symlink in the default gcc executable location `/usr/bin/gcc` , pointing to one of the installed gcc versions

````bash
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12 --slave /usr/bin/g++ g++ /usr/bin/g++-12
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 13 --slave /usr/bin/g++ g++ /usr/bin/g++-13
````

To change the gcc version, use  
`sudo update-alternatives --config gcc`

Passing g++ as `--slave` ensures that when `gcc` is updated, `g++` link is also updated
