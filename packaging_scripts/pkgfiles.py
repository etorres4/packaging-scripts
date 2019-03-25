"""Helper functions for dealing with package files."""

import logging
import re
import shutil

from pathlib import Path

# ========== Constants ==========
# Match any pkgfile of any name with the .pkg.tar.* extension
PKGREGEX = r"^\w+[.]pkg[.]tar([.]\w+)?$"
# Match any sigfile of any name with the .pkg.tar.*.sig extension
SIGREGEX = r"^\w+[.]pkg[.]tar([.]\w+)?[.]sig$"


# ========== Logging Setup ===========
syslog = logging.getLogger(__name__)


# ========== Functions ==========
def get(query=None, *, directory=None, signatures_only=False):
    """Return a list of package files in the current working directory.

    :param query: names of package files to search for
    :type query: str
    :param directory: a directory to search in
    :type directory: str or path-like object
    :param signatures_only: include only signature files
    :type signatures_only: bool
    :returns: paths of package files
    :rtype: list
    """
    path = Path.cwd() if directory is None else Path(directory)
    filequery = f"*{query}*" if query is not None else "*"

    if signatures_only:
        yield from _filter_by_regex(filequery, SIGREGEX, path)
    else:
        yield from _filter_by_regex(filequery, PKGREGEX, path)


def add(pkgfile, cachedir):
    """Add package file to the repository directory.

    :param pkg: path of package to add
    :type pkg: path-like object
    :param cachedir: cache directory to move package to
    :type cachedir: path-like object
    """
    syslog.info(f"Adding {pkgfile} to {cachedir}")
    shutil.move(pkgfile, cachedir / pkgfile.name)


def delete(pkg):
    """Remove package file.

    :param pkg: path of package to remove
    :type pkg: path-like object
    """
    pkg.unlink()
    syslog.info(f"Removed {pkg}")


def _filter_by_regex(query, regex_expression, path):
    """Filter package files only.

    :param query: names of package files to search for
    :type query: str
    :param regex_expression: the expression to filter by
    :type regex_expression: str
    :param path: directory to look for files
    :type path: path-like object
    :yields: package files from either the current working directory
        or an arbitrary directory
    """
    for pkgfile in path.glob(query):
        if re.match(regex_expression, str(pkgfile)):
            yield pkgfile
