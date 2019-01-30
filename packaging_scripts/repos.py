"""Module for pacman repository helper functions.
"""

import logging
import subprocess

# ========== Constants ==========
REPO_ADD_CMD = '/usr/bin/repo-add'
REPO_REMOVE_CMD = '/usr/bin/repo-remove'
DB_EXT = 'db.tar.xz'

# ========== Logging setup ==========
syslog = logging.getLogger(__name__)


# ========== Classes ==========
class RepoAddError(BaseException):
    """Exception when the repo-add or repo-remove script fails."""


# ========== Functions ==========
def repo_add(operation, db, *pkgs, opts=None):
    """Run repo-add.

    Since both the repo-add and repo-remove scripts have the
    same command-line usage, it is simpler to generalize both
    operations using a single function.

    :param operation: run repo-add or repo-remove, can be
        either 'add' or 'remove'
    :type operation: str
    :param db: the database file to operate on
    :type db: str, bytes, or path-like object
    :param opts: extra options to pass to repo-add
    :type opts: list
    :param pkgs: these arguments depend on whether the operation is
        an add or remove.
        If operation is 'add', then pkgs is all of the paths of the
        package files to add to the database. If operation is 'remove',
        then pkgs is the name of the packages to remove from the database.
    :type pkgs: any iterable
    :raises: RepoAddError if repo-add failed
    """

    if operation == 'add':
        syslog.info('Adding packages to database')
        cmd = [REPO_ADD_CMD]
    else:
        syslog.info('Removing packages from database')
        cmd = [REPO_REMOVE_CMD]

    syslog.debug(f"Options: {opts}")
    syslog.debug(f"Packages: {pkgs}")

    if opts is not None:
        cmd.extend(opts)

    cmd.append(db)
    cmd.extend(pkgs)
    syslog.debug(f"Final repo-add command: {cmd}")

    try:
        process = subprocess.run(cmd,
                                 check=True,
                                 capture_output=True,
                                 text=True)
    except RepoAddError:
        raise RepoAddError(process.stderr)
    else:
        syslog.debug(process.stdout)
        syslog.info('Finished adding packages to database')
