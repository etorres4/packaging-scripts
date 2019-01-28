"""Helper functions for dealing with package files."""

import pathlib

# ========== Constants ==========
PKGEXT = 'pkg.tar.xz'
SIGEXT = f"{PKGEXT}.sig"

# ========== Functions ==========
def get_pkgfiles(query, directory=None, signatures=False):
    """Return a list of package files in the current working directory.

    :param directory: a directory to search in
    :type directory: str, bytes, or path-like object
    :param signatures: include only signature files
    :type signatures: bool
    :returns: paths of package files
    :rtype: list
    """
    if directory is not None:
        path = pathlib.Path(directory)
    else:
        path = pathlib.Path.cwd()

    if signatures:
        return list(path.glob(f"{query}*.{SIGEXT}"))

    return list(path.glob(f"{query}*.{PKGEXT}"))
