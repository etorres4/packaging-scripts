"""Helper functions for dealing with package files."""

import glob
import os
import os.path

# ========== Constants ==========
PKGEXT = "pkg.tar.xz"
SIGEXT = f"{PKGEXT}.sig"


# ========== Functions ==========
def get_pkgfiles(query=None, directory=None, signatures_only=False):
    """Return a list of package files in the current working directory.

    :param query: names of package files to search for
    :type query: str
    :param directory: a directory to search in
    :type directory: str
    :param signatures_only: include only signature files
    :type signatures_only: bool
    :returns: paths of package files
    :rtype: list
    """
    if directory is not None:
        path = directory
    else:
        path = os.getcwd()

    if signatures_only and query is not None:
        return glob.glob(f"{path}/*{query}*.{SIGEXT}")
    elif signatures_only and query is None:
        return glob.glob(f"{path}/*.{SIGEXT}")
    elif not signatures_only and query is not None:
        return glob.glob(f"{path}/*{query}*.{PKGEXT}")
    elif not signatures_only and query is None:
        return glob.glob(f"{path}/*.{PKGEXT}")
