"""Helper functions for dealing with package files."""

import pathlib

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
    :rtype: generator
    """
    if directory is not None:
        path = pathlib.Path(directory)
    else:
        path = pathlib.Path.cwd()

    if signatures_only:
        if query is not None:
            return path.glob(f"{query}*.{SIGEXT}")
        else:
            return path.glob(f"*.{SIGEXT}")
    else:
        if query is not None:
            return path.glob(f"{query}*.{PKGEXT}")
        else:
            return path.glob(f"*.{PKGEXT}")
