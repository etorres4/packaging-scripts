"""Module for pacman repository helper functions.
"""

import logging
import subprocess

# ========== Logging setup ==========
syslog = logging.getLogger(__name__)


# ========== Classes ==========
class RepoAddError(BaseException):
    """Exception when the repo-add or repo-remove script fails."""


# ========== Functions ==========
def db_modify(operation, db, *args):
    """Run either repo-add or repo-remove.

    Since both the repo-add and repo-remove scripts have the
    same command-line usage, it is simpler to generalize both
    operations using a single function.

    :param operation: run repo-add or repo-remove, can be
        either 'add' or 'remove'
    :type operation: str
    :param db: the database file to operate on
    :type db: str, bytes, or path-like object
    :param args: These arguments include two things:
        * Extra options to pass to repo-add
        * Package names
          Package names can further be divided into two types depending
          on the operation. Adding requires that the paths to the package
          files are passed. Removing requires that the names of the packages
          are passed.
    :type args: str
    :raises: RepoAddError if repo-add failed
    :raises: ValueError if an invalid operation was specified
    """
    if operation == "add":
        syslog.info("Adding packages to database")
    elif operation == "remove":
        syslog.info("Removing packages from database")
    else:
        raise ValueError(f"Invalid operation specified: {operation}")

    syslog.debug(f"Database: {db}")
    syslog.debug(f"Arguments: {args}")

    try:
        process = _run_script(operation, str(db), *args)
    except subprocess.CalledProcessError as e:
        raise RepoAddError(e)
    else:
        syslog.debug(process.stdout)
        syslog.info("Database operation complete")


def _run_script(operation, *args):
    """Run either the repo-add or the repo-remove script.

    :param operation: run either repo-add or repo-remove; can be either
        'add' or 'remove'
    :type operation: str
    :param args: arguments to pass to repo-add script; can be both
        options and packages
    :type args: str
    """
    return subprocess.run(
        (f"repo-{operation}", *args), check=True, capture_output=True, text=True
    )
