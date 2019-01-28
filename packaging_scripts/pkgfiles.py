"""Helper functions for dealing with package files."""

import pathlib

PKGEXT = 'pkg.tar.xz'
SIGEXT = f"{PKGEXT}.sig"

def get_pkgfiles(directory=None, signatures=False):
    """Return a list of package files in the current working directory.

    :param directory: a directory to search in
    :type directory: str, bytes, or path-like object
    :returns: paths of package files
    :rtype: list
    """
    if directory:
        path = pathlib.Path(directory)
    else:
        path = pathlib.Path.cwd()

    if signatures:
        return list(path.glob(f"*.{SIGEXT}"))

    return list(path.glob(f"*.{PKGEXT}"))
