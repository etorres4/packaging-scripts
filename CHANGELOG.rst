Changelog for packaging-scripts
===============================

Version 1.6.1
-------------

* pug2

  * Add description to help message

Version 1.6.0
-------------

* pug2

  * Add --check-if-enabled option for running with pacman hook

Version 1.6.0
-------------

* pug2

  * Print error messages from gist when necessary

  * Hook: add packaging-scripts as dependency


Version 1.5.3
-------------

* Project

  * PKGBUILD: make use of pkgver()

  * packaging-scripts.conf: remove quotes from empty settings

* pug2

  * Compare package lists before updating gist version

Version 1.5.2
-------------

* pug2

    * Initial full implementation of the pug2 script

    * Create config file section for pug2 options

Version 1.5.1
-------------

* pug2

  * Add repository name to filename when uploading to gist

Version 1.5
-----------

* Project

  * PKGBUILD: build from git repository directly

  * Rename pacmanconf module to pacman

  * Add config file to /etc

  * Add pug2 script

Version 1.4
-----------

* Project

  * Add CHANGELOG

  * Minor code and comment cleanups

  * Use % formatting for log messages instead of f-strings

  * setup.py: Add command to build sphinx docs and update packages accordingly

  * Comments: fix incorrect ':raises:' docstrings

  * Tests: incorporate hypothesis test framework and simplify tests

* packaging_scripts.pacmanconf

  * Delete 'options' section from config sections directly

* packaging_scripts.pkgfiles
  
  * PKGREGEX and SIGREGEX: account for colons in package version numbers

  * Directly import pathlib.Path instead of pathlib module entirely


Version 1.3.1
-------------

* Project

  * setup.py: use setuptools.find_packages() to locate packages

  * Move tests to packaging_scripts package

* packaging_scripts.pkgfiles

  * Account for duplicate elements in the iterable passed to filter()


Version 1.3
-----------

* Project

  * README: Add internal implementation notes

* Scripts

  * addpkg: change package file type parsing for files passed through command line

* packaging_scripts.pkgfiles

  * Add ability to filter through iterables


Version 1.2
-----------

* Project

  * Untrack PKGBUILD

  * Update gitignore

  * AppArmor profiles: update to include $XDG_CACHE_HOME/aurutils/sync

* Scripts

  * addpkg, delpkg: add --files-only option

  * delpkg: update help message for -c flag

* packaging_scripts.pkgfiles

  * Depend only on pathlib and re modules

  * Make signatures_only in get_pkgfiles() a required kwarg

  * Move add and delete functionality to this module, and add tests

  * Update regexes for more accurate matches

* packaging_scripts.repos

  * db_modify(): add support for path-like objects


Version 1.1.2
-------------

* Project

  * Add AppArmor profiles for addpkg and delpkg scripts


Version 1.1
-----------

* Project

  * README: add emblem for python-black code formatter

  * LICENSE: add file and specify MIT license

  * Run black python formatting utility on all .py source files

  * Do not ignore PKGBUILD

* Scripts

  * addpkg, delpkg: add new flags -c and -d for overriding cachedir and database filenames

  * addpkg, delpkg: make the assumption that a repo's database file has the same name as that repo i.e. aur would have aur.db as its database file, rewrite file naming code accordingly


Version 1.0.2
-------------

* Project

  * Remove git version-checking code from setup.py

* packaging_scripts.repos

  * Do not pass None to db_modify()

* Scripts

  * addpkg, delpkg: Fix incorrect reference to database file in f-strings


Version 1.0
-----------

* Project

  * Add README

* Scripts

  * Reimplement in python 3

  * addpkg, delpkg: make calls to console_handler instead of stdout_handler

  * addpkg, delpkg: split console logging between stdout and stderr

  * delpkg: include missing sys import

* Make use of os instead of shutil for move operations

* packaging_scripts.pkgfiles

  * Utilize os.path instead of pathlib

  * Use glob and os.path modules for filename handling

  * get_pkgfiles(): make if statement that checks directory arguments more explicit

  * get_pkgfiles(): Add info to docstring

* packaging_scripts.repos

  * Add module

  * Reimplement repo_add() as db_modify() and update code accordingly

  * db_modify(): don't call subprocess.CompletedProcess.stdout out-of-scope when raising RepoAddError

  * gen_cmdline(): make ValueError message more clear

  * gen_cmdline(): stop erroneous raising of ValueError on command checking
