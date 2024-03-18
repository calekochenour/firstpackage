import nox

###############################################################################
# Using venv - have to have python versions already installed
# From hatch shell
#
# To run:
# >>> nox --session test
###############################################################################


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def test(session):
    # install - needed if there are test dependencies
    #  (should already be installed for my config)
    # session.install(".[tests]")
    session.install(".")
    # Run tests
    session.run("pytest")


###############################################################################
# Using conda/mamba - will create/download  python versions
# From non-hatch shell (with pytest?)
#
# WORKING
#
# To run:
# >>> nox --session test_conda
###############################################################################


@nox.session(venv_backend="conda", python=["3.9", "3.10", "3.11", "3.12"])
def test_conda(session):
    """Nox function that installs dev requirements and runs
    tests on Python 3.8 through 3.12
    """
    # Install dev requirements
    # session.conda_install(".[tests]", channel='conda-forge')
    session.install(".")
    session.install("pytest")
    # session.install('pytest-cov', '--no-deps')
    # Run tests using any parameters that you need
    session.run("pytest")
