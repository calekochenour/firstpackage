# Reference Guide

| <!-- --> | <!-- --> |
|---|---|
| **Envrionment Setup** ||  |
| Set PowerShell execution policy | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Install Scoop | `Invoke-RestMethod -Uri https://get.scoop.sh \| Invoke-Expression` |
| Add "main" bucket as download source | `scoop bucket add main` |
| Add "versions" bucket as download source | `scoop bucket add versions` |
| Install pipx | `scoop install pipx`or `scoop install main/pipx` |
| Install python | `scoop install python` or `scoop install main/python` |
| Install specific python version | `scoop install versions/python311` |
| Update PATH variable with pipx directory | `pipx ensurepath` |
| Install hatch | `pipx install hatch` |
| List hatch commands | `hatch -h` |
| Open location of hatch config file | `hatch config explore` |
| Print contents of hatch config file | `hatch config show` |
| Install grayskull | `pipx install grayskull` |
| **Package Development** ||  |
| Create package structure and baseline contents | `hatch new [PACKAGE_NAME]` |
| Install package locally in editable mode | `python -m pip install -e .` |
| List packages installed in current environment | `pip list` |
| Install package from GitHub | `pip install git+https://github.com/user/repo.git@branch_or_tag` |
| Create development environment | `hatch env create` |
| Activate development environment | `hatch shell` |
| Exit development envrironment | `exit` |
| **Package Publishing** ||  |
| Build package sdist and wheel distributions | `hatch build` |
| Publish package to Test PyPI | `hatch publish -r test` |
| Install package from Test PyPI | `pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME]` |
| Publish package to PyPI | `hatch publish` |
| Install package from PyPI | `pip install -i https://pypi.org/simple/ [PACKAGE_NAME]` |
| Create conda-forge recipe | `grayskull pypi [PACKAGE_NAME]` |
| Check that package installs properly | `pip check` |
| Install package from conda-forge | `conda install -c conda-forge [PACKAGE_NAME]` |
