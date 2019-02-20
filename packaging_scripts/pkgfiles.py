"""Helper functions for dealing with package files."""

import glob
import os
import os.path

# ========== Constants ==========
PKGEXT = 'pkg.tar.xz'
SIGEXT = f"{PKGEXT}.sig"


# ========== Functions ==========
def get_pkgfiles(query=None, directory=None, signatures_only=False):
    """Return a list of package files in the current working directory.

    :param query: names of package files to search for
    :type query: str
    :param directory: a directory to search in
    :type directory: str, bytes, or path-like object
    :param signatures_only: include only signature files
    :type signatures_only: bool
    :returns: paths of package files
    :rtype: list
    """
    if directory is not None:
        path = directory
    else:
        path = os.getcwd()

    if signatures_only:
        if query is not None:
            return glob.glob(f"{path}/{query}*.{SIGEXT}")
        else:
            return glob.glob(f"{path}/*.{SIGEXT}")
    else:
        if query is not None:
            return glob.glob(f"{path}/{query}*.{PKGEXT}")
        else:
            return glob.glob(f"{path}/*.{PKGEXT}")
