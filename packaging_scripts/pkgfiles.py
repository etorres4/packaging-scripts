"""Helper functions for dealing with package files."""

import logging
import re
import shutil

from pathlib import Path

# ========== Constants ==========
# Match any pkgfile of any name with the .pkg.tar.* extension
PKGREGEX = r"^[\w.+/-]+\.pkg\.tar(\.\w+)?$"
# Match any sigfile of any name with the .pkg.tar.*.sig extension
SIGREGEX = r"^[\w.+/-]+\.pkg\.tar(\.\w+)?\.sig$"


# ========== Logging Setup ===========
syslog = logging.getLogger(__name__)


# ========== Functions ==========
def get(query=None, *, directory=None, signatures_only=False):
    """Retrieve all package-related files from the filesystem.

    :param query: names of package files to search for
    :type query: str
    :param directory: a directory to search in
    :type directory: str or path-like object
    :param signatures_only: include only signature files
    :type signatures_only: bool
    :yields: paths of package files
    """
    path = Path.cwd() if directory is None else Path(directory)
    filequery = f"*{query}*" if query else "*"

    if signatures_only:
        yield from _filter_by_regex(SIGREGEX, path.glob(filequery))
    else:
        yield from _filter_by_regex(PKGREGEX, path.glob(filequery))


def filter(iterable, *, signatures_only=False):
    """Retrive package file types from a predefined iterable.

    :param iterable: any iterable
    :type iterable: anything that returns str or path-like objects
    :param signatures_only: include only signature files
    :type signatures_only: bool
    :yields: paths of package files
    """
    if signatures_only:
        yield from _filter_by_regex(SIGREGEX, sorted(set(iterable)))
    else:
        yield from _filter_by_regex(PKGREGEX, sorted(set(iterable)))


def add(pkgfile, cachedir):
    """Add package file to the repository cache directory.

    :param pkg: path of package to add
    :type pkg: path-like object
    :param cachedir: cache directory to move package to
    :type cachedir: path-like object
    """
    syslog.info("Adding %s to %s", pkgfile, cachedir)
    shutil.move(pkgfile, cachedir / pkgfile.name)


def delete(pkg):
    """Remove package file.

    :param pkg: path of package to remove
    :type pkg: path-like object
    """
    pkg.unlink()
    syslog.info("Removed %s", pkg)


def _filter_by_regex(regex_expression, iterable):
    """Filter by regular expression.

    :param regex_expression: the expression to filter by
    :type regex_expression: str
    :param iterable: iterable to filter through
    :type iterable: str or path-like objects
    :yields: pathlib.Path objects to package files
    """
    for item in iterable:
        if re.match(regex_expression, str(item)):
            yield Path(item)
