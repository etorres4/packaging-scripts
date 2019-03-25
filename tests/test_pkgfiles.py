import packaging_scripts.pkgfiles as pkgfiles
import re
import unittest

from pathlib import Path
from types import GeneratorType
from unittest.mock import patch


# ========== Constants ==========
TESTING_MODULE = f"packaging_scripts.pkgfiles"
# Match any pkgfile of any name with the .pkg.tar.* extension
PKGREGEX = "^[\w]+[.]pkg[.]tar([.][\w]+)?$"
# Match any sigfile of any name with the .pkg.tar.*.sig extension
SIGREGEX = '^.+[.]pkg[.]tar[.].+[.]sig$'

ALL_PKGFILES = [
        Path("pkg1.pkg.tar.xz"),
        Path("pkg1.pkg.tar.xz.sig"),
        Path("pkg2.pkg.tar.xz"),
        Path("pkg3.pkg.tar.xz"),
        Path("pkg3.pkg.tar.xz.sig"),
        Path('notapkg.sig'),
]


# ========== Functions ==========
def get_all_files(*args):
    for f in ALL_PKGFILES:
        yield f


def filter_files(query):
    for f in [
            Path("pkg3.pkg.tar.xz"),
            Path("pkg3.pkg.tar.xz.sig"),
    ]:
        yield f


# ========== Unit Tests ==========
class TestFilterPkgfiles(unittest.TestCase):
    def setUp(self):
        self.patched_path = patch.object(Path, "glob")
        self.mocked_glob = self.patched_path.start()

        self.mocked_glob.side_effect = get_all_files

    def test_yield_no_query(self):
        result = pkgfiles.get_pkgfiles()
        expected = [s for s in get_all_files() if re.match(PKGREGEX, str(s))]

        self.assertListEqual(list(result), expected)
        self.assertIsInstance(result, GeneratorType)

    def test_yield_with_query(self):
        self.mocked_glob.side_effect = filter_files

        result = pkgfiles.get_pkgfiles('pkg3')
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
        result = pkgfiles.get_pkgfiles(signatures_only=True)
        expected = [s for s in get_all_files() if re.match(SIGREGEX, str(s))]

        self.assertListEqual(list(result), expected)
        self.assertIsInstance(result, GeneratorType)

    def test_yield_with_query(self):
        self.mocked_glob.side_effect = filter_files

        result = pkgfiles.get_pkgfiles('pkg3', signatures_only=True)
        expected = [Path("pkg3.pkg.tar.xz.sig")]

        self.assertListEqual(list(result), expected)
        self.assertIsInstance(result, GeneratorType)

    def tearDown(self):
        self.patched_path.stop()
