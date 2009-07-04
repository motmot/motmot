#!/bin/bash

# abort on error
set -o errexit

VIRTUALENVDIR=PYtest

# clean old virtual environment
rm -rf $VIRTUALENVDIR

# build new virutal environment
virtualenv $VIRTUALENVDIR

# activate new virutal environment
source $VIRTUALENVDIR/bin/activate

# ensure there exists a setup.py script (even if it does nothing)
git submodule foreach "touch setup.py"

# build all packages
DISABLE_INSTALL_REQUIRES=1 git submodule foreach "python setup.py develop"
