.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

Packaging Scripts
=================

The Scripts
-----------
* addpkg - add a package to a repository and then automatically move its package tarfiles to that repository's respective cache directory
* delpkg - remove a package from a repository by manipulating the db file, and then remove that respective package's tarballs in that repository's directory
* fqo ("fuzzy pacman -Qo") - using fzf and mlocate, select a file and then pass that file to $(pacman -Qo)

addpkg
^^^^^^
* Either take all pacman package files in the current working directory or from the command line and add them to the given repository
* Automatically move said package files to the repository's cache directory

delpkg
^^^^^^
* Take the names of packages and a repository, then delete those packages from said repository
* Automatically delete all tarfiles of those packages from the repository

fqo
^^^
* Given a query, pass to locate and then pass the results to fzf
* Select a file and then pass that file to pacman -Qo

Implementation Notes
--------------------
* All code internally uses pathlib for path handling
