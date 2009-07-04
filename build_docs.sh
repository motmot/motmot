#!/bin/bash

# abort on error
set -o errexit

VIRTUALENVDIR=PYtest

# activate new virutal environment
source $VIRTUALENVDIR/bin/activate

cd doc

make clean
make html
