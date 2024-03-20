# Reference Guide

| Description | Syntax |
|---|---|
| Set PowerShell execution policy | Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser |
| Install Scoop | Invoke-RestMethod -Uri https://get.scoop.sh \| Invoke-Expression |
| Add "main" bucket as download source (default / primary source) | scoop bucket add main |
| Add "versions" bucket as download source (non-primary source) | scoop bucket add versions |
| Install pipx (latest stable version) | scoop install pipx OR scoop install main/pipx |
| Install python (latest stable version) | scoop install python OR scoop install main/python |
| Install specific python version (non-latest) | scoop install versions/python311 |
| Update PATH variable with pipx directory | pipx ensurepath |
| Install hatch | pipx install hatch |
| List hatch commands | hatch -h |
| Open location of hatch config file | hatch config explore |
| Print contents of hatch config file | hatch config show |
| Create Python package structure and baseline contents | hatch new [PACKAGE_NAME] |
| Install Python package locally in editable mode | python -m pip install -e . |
| List packages installed in current environment | pip list |
| Install package from GitHub | pip install git+https://github.com/user/repo.git@branch_or_tag |
| Create a development environment with package in editable mode and all dependencies | hatch env create |
| Activate development environment | hatch shell |
| Exit development envrironment | exit |
| Build package sdist and wheel distributions | hatch build |
| Publish package to Test PyPI | hatch publish -r test |
| Install package from Test PyPI | pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME] |
| Publish package to PyPI | hatch publish |
| Install package from PyPI | pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME] |
| Install grayskull | pipx install grayskull |
| Create conda-forge recipe | grayskull pypi [PACKAGE_NAME] |
| Check that package installs properly with dependencies | pip check |
| Install package from conda-forge | conda install -c conda-forge [PACKAGE_NAME] |
