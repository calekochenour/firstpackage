# firstpackage

[![PyPI - Version](https://img.shields.io/pypi/v/firstpackage.svg)](https://pypi.org/project/firstpackage)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/firstpackage.svg)](https://pypi.org/project/firstpackage)

-----

**Table of Contents**

- [firstpackage](#firstpackage)
  - [Installation](#installation)
  - [License](#license)
  - [Cheatsheat / Global Setup / Windows 10](#cheatsheat--global-setup--windows-10)
    - [Environment Setup](#environment-setup)
    - [`hatch` config.toml](#hatch-configtoml)
    - [Package Setup](#package-setup)
    - [Pacakge Build](#pacakge-build)
    - [Test PyPI](#test-pypi)
    - [Operational PyPI](#operational-pypi)
    - [conda-forge](#conda-forge)
    - [Useful commands](#useful-commands)

## Installation

```console
pip install firstpackage
```

## License

`firstpackage` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Cheatsheat / Global Setup / Windows 10

### Environment Setup

This contains the commands used to set up the workflow environment from start to fisish (thorugh Test PyPi). For the full context, see the pyOpenSci documention.

Initial setup (for global use):

* Need `hatch` for project/package management
* Install `scoop`
* Use `scoop` to install `pipx`
* (Optional) Use `scoop` to install Python
* Use `pipx` to install `hatch`  

```
scoop --> pipx --> hatch
```

Ready for `hatch setup`. **Note:** You may need to close/reopen the terminal and/or log out/in from your Windows account multiple times through the entire process. If things don't appear to work, try either or both.

```
> example-command

 You will need to open a new terminal or re-login for the PATH changes to take effect.
```


Install `scoop` (Windoes PowerShell, non-admin):

```
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

```
> Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

Use `scoop` to install `pipx` (regular terminal, cmd or from IDE, for this and all other commands):

```
> scoop install pipx
```

or

```
> scoop install main/pipx
```

then

```
> pipx ensurepath
```


(Optional) Use `scoop` to install Python (if `pipx ensurepath` returns the following error):

```
> pipx ensurepath

  Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
```

```
> scoop install python
```

or

```
> scoop install main/python
```


Use `pipx` to install `hatch`:

```
pipx install hatch
```

### `hatch` config.toml

Open location of `hatch` config:

```
> hatch config explore
```

Print contents of `hatch` config:

```
> hatch config show
```

Manual tasks:
* Update hatch config with name email (manual process)

### Package Setup

Create/initialize package structure/contents:

```
hatch new [PACKAGE_NAME]
```


Manual tasks:

* Add python code to src/[PACKAGE_NAME]/
* Update/modify `pyproject.toml` as needed

Install PACKAGE_NAME locally (editable mode), can be `venv`, `conda` or `pip`

```
> python -m pip install -e .
```

or via github

```
> pip install git+https://github.com/user/repo.git@branch_or_tag
```

Manual tasks:

* Test funtionality of installed package locally

### Pacakge Build

Create development environment:

```
> hatch shell
```

See what's installed:

```
pip list
```

Build package (sdist, wheel):

```
hatch build
```

### Test PyPI

Manual tasks:

* Set up test PyPI account
* Create API token for upload

Upload to test PyPI:

```
hatch publish -r test
```

usename = `__token__`

Install package into env:

Conda
```
> conda activate pyospkg-dev
> pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME]
> conda list
```

or (venv mac/Linux)

```
> hatch shell
> pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME]
> pip list
```

### Operational PyPI

Manual tasks:

* Set up PyPI account
* Create API token for upload

Upload to PyPI:

```
hatch publish
```

usename = `__token__`

Install package into env:

Conda
```
> conda activate pyospkg-dev
> pip install -i https://pypi.org/simple/ [PACKAGE_NAME]
> conda list
```

or (venv mac/Linux)

```
> hatch shell
> pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME]
> pip list
```

### conda-forge

Install grayskull:
```
> pipx install grayskull
```

Manual tasks:

* Fork and clone the conda-forge staged-recipes [repo](https://github.com/conda-forge/staged-recipes)
* Create new branch as [PACKAGE_NAME]
* Checkout new branch

Create conda-forge recipe:

```
> grayskull pypi [PACKAGE_NAME]
```

Recipe located `recipes/[PACKAGE_NAME]}/meta.yaml`

Manual task:

* Add "home" section to `meta.yml` file (current bug in grayskull)

```
about:
  home: https://pypi.org/project/pyospackage/
  summary: A package that adds numbers together
  dev_url: https://github.com/pyopensci/pyospackage
  license: BSD-3-Clause
  license_file: LICENSE
```

Local tests:

* Try to import main module (or others)
  * `> import PACKAGE_NAME`
* Ensure package installs properly
  * `> pip check`

Manual tasks:

* Submit a pull request from your fork/branch to conda-forge/staged-recipes repository

Install from conda-forge:

```
> conda install -c conda-forge [PACKAGE_NAME]
```

### Useful commands

Update packages downloaded from scoop (PowerShell):
* `scoop update`

Reinstall latest PACKAGE_NAME version:
* `python -m pip install PACKAGE_NAME -e .`

Show packages in hatch env:
* `pip list`

View all environments hatch has access to:
* `hatch env show`

Print path to active hatch env (for use with IDE env config):
* `hatch env find`

Exit hatch env:
* `exit`
