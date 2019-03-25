import packaging_scripts.pkgfiles as pkgfiles
import re
import unittest

from pathlib import Path
from types import GeneratorType
from unittest.mock import MagicMock, patch


# ========== Constants ==========
TESTING_MODULE = f"packaging_scripts.pkgfiles"
# Match any pkgfile of any name with the .pkg.tar.* extension
PKGREGEX = r"^[\w.+/-]+\.pkg\.tar(\.\w+)?$"
# Match any sigfile of any name with the .pkg.tar.*.sig extension
SIGREGEX = r"^[\w.+/-]+\.pkg\.tar(\.\w+)?\.sig$"

ALL_PKGFILES = [
    Path("pkg1.pkg.tar.xz"),
    Path("pkg1.pkg.tar.xz.sig"),
    Path("pkg2.pkg.tar.xz"),
    Path("pkg3.pkg.tar.xz"),
    Path("pkg3.pkg.tar.xz.sig"),
    Path("notapkg.sig"),
]


# ========== Functions ==========
def get_all_files(*args):
    for f in ALL_PKGFILES:
        yield f


def filter_files(query):
    for f in [Path("pkg3.pkg.tar.xz"), Path("pkg3.pkg.tar.xz.sig")]:
        yield f


# ========== Unit Tests ==========
class TestFilterPkgfiles(unittest.TestCase):
    def setUp(self):
        self.patched_path = patch.object(Path, "glob")
        self.mocked_glob = self.patched_path.start()

        self.mocked_glob.side_effect = get_all_files

    def test_yield_no_query(self):
        result = pkgfiles.get()
        expected = [s for s in get_all_files() if re.match(PKGREGEX, str(s))]

        self.assertListEqual(list(result), expected)
        self.assertIsInstance(result, GeneratorType)

    def test_yield_with_query(self):
        self.mocked_glob.side_effect = filter_files

        result = pkgfiles.get("pkg3")
        expected = [Path("pkg3.pkg.tar.xz")]

        self.assertListEqual(list(result), expected)
        self.assertIsInstance(result, GeneratorType)

    def tearDown(self):
        self.patched_path.stop()


class TestFilterSigfiles(unittest.TestCase):
    def setUp(self):
        self.patched_path = patch.object(Path, "glob")
        self.mocked_glob = self.patched_path.start()

        self.mocked_glob.side_effect = get_all_files

    def test_yield_no_query(self):
        result = pkgfiles.get(signatures_only=True)
        expected = [s for s in get_all_files() if re.match(SIGREGEX, str(s))]

        self.assertListEqual(list(result), expected)
        self.assertIsInstance(result, GeneratorType)

    def test_yield_with_query(self):
        self.mocked_glob.side_effect = filter_files

        result = pkgfiles.get("pkg3", signatures_only=True)
        expected = [Path("pkg3.pkg.tar.xz.sig")]

        self.assertListEqual(list(result), expected)
        self.assertIsInstance(result, GeneratorType)

    def tearDown(self):
        self.patched_path.stop()


class TestAddPkgfile(unittest.TestCase):
    def setUp(self):
        self.patched_shutil = patch(f"{TESTING_MODULE}.shutil")
        self.mocked_shutil = self.patched_shutil.start()

        self.pkgfile = Path("/home/user/pkgfile")
        self.cachedir = Path("/var/cache/repo")

    def test_pkgfile_path(self):
        pkgfiles.add(self.pkgfile, self.cachedir)

        self.mocked_shutil.move.assert_called_with(
            self.pkgfile, Path("/var/cache/repo/pkgfile")
        )

    def tearDown(self):
        self.patched_shutil.stop()


class TestDeletePkgfiles(unittest.TestCase):
    def setUp(self):
        self.pkgfile = MagicMock("/var/cache/repo/pkgfile", spec_set=Path)

    def test_delete(self):
        pkgfiles.delete(self.pkgfile)

        self.pkgfile.unlink.assert_called()
