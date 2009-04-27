The motmot packages
===================

Please see the documentation overview in doc/source/index.rst.

Our homepage is http://code.astraw.com/projects/motmot

To download all packages from github
====================================

The motmot packages are stored using git submodules__. To get a copy
of the entire repository::

  git clone git://github.com/motmot/motmot.git
  cd motmot
  git submodule update --init

To update all packages from github::

  git fetch
  git merge origin/master
  git submodule update --init
  git submodule update

(Note that this changes what is checked out in the submodules, and may
result in a detached HEAD! You may want to do ``git checkout master``
in the newly updated submodule directories.)

To add a new submodule, upload it normally to github. Then, add
it. For example, with pycamiface, this was used:

  git submodule add git://github.com/motmot/pycamiface.git pycamiface

__ http://www.kernel.org/pub/software/scm/git/docs/git-submodule.html
