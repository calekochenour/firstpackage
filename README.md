# firstpackage

<!-- [![PyPI - Version](https://img.shields.io/pypi/v/firstpackage.svg)](https://pypi.org/project/firstpackage)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/firstpackage.svg)](https://pypi.org/project/firstpackage) -->

<!-- ----- -->

**Table of Contents**

- [firstpackage](#firstpackage)
  - [License](#license)
  - [Resources](#resources)
  - [Reference Guide / Global Setup / Windows 10](#reference-guide--global-setup--windows-10)
    - [Environment Setup](#environment-setup)
    - [hatch config.toml](#hatch-configtoml)
    - [Package Setup](#package-setup)
    - [Package Build](#package-build)
    - [Test PyPI](#test-pypi)
    - [Operational PyPI](#operational-pypi)
    - [conda-forge](#conda-forge)
    - [Useful commands](#useful-commands)

<!-- ## Installation

```console
pip install firstpackage
``` -->

## License

`firstpackage` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Resources

This repository followed the steps in the [pyOpenSci Python Package Guide](https://www.pyopensci.org/python-package-guide/) to create an example Python package from start to completion, stopping after the package was uploaded to test PyPI.

The reference guide listed below is a condensed form of the instructions, with the necessary commands and actions to complete this process (tested through the upload to test PyPI). The commands are provided without context, which is intended, as a way to contain all of the necessary steps to complete the process in a summarized form. For the full context and explanations of the "what" and "why", please see the pyOpenSci documentation.

- [pyOpenSci Tutorials](https://www.pyopensci.org/python-package-guide/tutorials/intro.html)
- [pyOpenSci Documentation](https://www.pyopensci.org/python-package-guide/documentation/index.html)
- [pyOpenSci Packaging](https://www.pyopensci.org/python-package-guide/package-structure-code/intro.html)
- [pyOpenSci Tests](https://www.pyopensci.org/python-package-guide/tests/index.html)

## Reference Guide / Global Setup / Windows 10

### Environment Setup

This contains the commands used to set up the workflow environment from start to fisish (thorugh Test PyPi). For the full context, see the pyOpenSci documention.

Initial setup (for global use):

- Need `hatch` for project/package management
- Install `scoop`
- Use `scoop` to install `pipx`
- (Optional) Use `scoop` to install Python
- Use `pipx` to install `hatch`  

```console
scoop --> pipx --> hatch
```

Ready for `hatch setup`. **Note:** You may need to close/reopen the terminal and/or log out/in from your Windows account multiple times through the entire process. If things don't appear to work, try either or both.

```console
> example-command

 You will need to open a new terminal or re-login for the PATH changes to take effect.
```

Install `scoop` (PowerShell, non-admin):

```console
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

```console
> Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

Use `scoop` to install `pipx` (regular terminal, cmd or from IDE, for this and all other commands):

```console
> scoop install pipx
```

or

```console
> scoop install main/pipx
```

then

```console
> pipx ensurepath
```

(Optional) Use `scoop` to install Python (if `pipx ensurepath` returns the following error):

```console
> pipx ensurepath

  Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
```

```console
> scoop install python
```

or

```console
> scoop install main/python
```

Use `pipx` to install `hatch`:

```console
pipx install hatch
```

### hatch config.toml

Open location of `hatch` config:

```console
> hatch config explore
```

Print contents of `hatch` config:

```console
> hatch config show
```

Manual tasks:

- Update hatch config with name and email

### Package Setup

Create/initialize packagedd structure/contents:

```conesole
hatch new [PACKAGE_NAME]
```

Manual tasks:

- Add python code to src/[PACKAGE_NAME]/
- Update/modify `pyproject.toml` as needed

Install PACKAGE_NAME locally (editable mode), can be `venv`, `conda` or `pip`

```console
> python -m pip install -e .
```

or via github

```console
> pip install git+https://github.com/user/repo.git@branch_or_tag
```

Manual tasks:

- Test functionality of installed package locally

### Package Build

Create development environment:

```console
> hatch shell
```

See what's installed:

```console
pip list
```

Build package (sdist, wheel):

```console
hatch build
```

### Test PyPI

Manual tasks:

- Set up test PyPI account
- Create API token for upload

Upload to test PyPI:

```console
hatch publish -r test
```

usename = `__token__`

Install package into env:

Conda

```console
> conda activate pyospkg-dev
> pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME]
> conda list
```

or (venv mac/Linux)

```console
> hatch shell
> pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME]
> pip list
```

### Operational PyPI

Manual tasks:

- Set up PyPI account
- Create API token for upload

Upload to PyPI:

```console
hatch publish
```

username = `__token__`

Install package into env:

Conda

```console
> conda activate pyospkg-dev
> pip install -i https://pypi.org/simple/ [PACKAGE_NAME]
> conda list
```

or (venv mac/Linux)

```console
> hatch shell
> pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME]
> pip list
```

### conda-forge

Install grayskull:

```cconsole
> pipx install grayskull
```

Manual tasks:

- Fork and clone the conda-forge staged-recipes [repo](https://github.com/conda-forge/staged-recipes)
- Create new branch as [PACKAGE_NAME]
- Checkout new branch

Create conda-forge recipe:

```console
> grayskull pypi [PACKAGE_NAME]
```

Recipe located `recipes/[PACKAGE_NAME]}/meta.yaml`

Manual task:

- Add "home" section to `meta.yml` file (current bug in grayskull)

```console
about:
  home: https://pypi.org/project/pyospackage/
  summary: A package that adds numbers together
  dev_url: https://github.com/pyopensci/pyospackage
  license: BSD-3-Clause
  license_file: LICENSE
```

Local tests.

Try to import main module (or others):

```console
> import PACKAGE_NAME
```

Ensure package installs properly:

```console
> pip check
```

Manual tasks:

- Submit a pull request from your fork/branch to conda-forge/staged-recipes repository

Install from conda-forge:

```console
> conda install -c conda-forge [PACKAGE_NAME]
```

### Useful commands

Update packages downloaded from scoop (PowerShell):

```console
> scoop update
```

Reinstall latest PACKAGE_NAME version:

```console
> python -m pip install PACKAGE_NAME -e .
```

Show packages in hatch env:

```console
> pip list
```

View all environments hatch has access to:

```console
> hatch env show
```

Print path to active hatch env (for use with IDE env config):

```console
> hatch env find
```

Exit hatch env:

```console
exit
```
