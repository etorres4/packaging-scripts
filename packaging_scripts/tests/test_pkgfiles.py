import packaging_scripts.pkgfiles as pkgfiles
import re
import unittest

from hypothesis import given
from hypothesis.strategies import iterables, text
from pathlib import Path
from types import GeneratorType
from unittest.mock import MagicMock, patch


# ========== Constants ==========
TESTING_MODULE = f"packaging_scripts.pkgfiles"
# Match any pkgfile of any name with the .pkg.tar.* extension
PKGREGEX = r"^[\w.+/-]+\.pkg\.tar(\.\w+)?$"
# Match any sigfile of any name with the .pkg.tar.*.sig extension
SIGREGEX = r"^[\w.+/-]+\.pkg\.tar(\.\w+)?\.sig$"


# ========== Unit Tests ==========
class TestFilterByRegex(unittest.TestCase):
    @given(iterables(text()))
    def test_pkgregex(self, i):
        result = pkgfiles._filter_by_regex(pkgfiles.PKGREGEX, i)
        expected = [Path(p) for p in i if re.match(PKGREGEX, str(p))]

        self.assertListEqual(sorted(result), expected)
        self.assertIsInstance(result, GeneratorType)

    @given(iterables(text()))
    def test_sigregex(self, i):
        result = pkgfiles._filter_by_regex(pkgfiles.SIGREGEX, i)
        expected = [Path(p) for p in i if re.match(SIGREGEX, str(p))]

        self.assertListEqual(list(result), expected)
        self.assertIsInstance(result, GeneratorType)


class TestAddPkgfile(unittest.TestCase):
    def setUp(self):
        self.patched_shutil = patch(f"{TESTING_MODULE}.shutil")
        self.mocked_shutil = self.patched_shutil.start()

    @given(text())
    def test_pkgfile_path(self, p):
        pkgfile = Path(p)
        cachedir = Path("/var/cache/repo")

        pkgfiles.add(pkgfile, cachedir)

        self.mocked_shutil.move.assert_called_with(
            pkgfile, Path(f"/var/cache/repo/{pkgfile.name}")
        )

    def tearDown(self):
        self.patched_shutil.stop()


class TestDeletePkgfile(unittest.TestCase):
    def setUp(self):
        self.pkgfile = MagicMock("/var/cache/repo/pkgfile", spec_set=Path)

    def test_delete(self):
        pkgfiles.delete(self.pkgfile)

        self.pkgfile.unlink.assert_called()
