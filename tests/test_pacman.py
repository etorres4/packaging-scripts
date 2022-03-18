import packaging_scripts.pacman as pacman
import re
import unittest

from hypothesis import given
from hypothesis.strategies import iterables, text
from pathlib import Path
from types import GeneratorType
from unittest.mock import MagicMock, patch


# ========== Constants ==========
TESTING_MODULE = f"packaging_scripts.pacman"


# ========== Unit Tests ==========
# class TestParseConfigFile(unittest.TestCase):
#    def setUp(self):
#        self.pat
#
#    def tearDown(self):
#
#
# class TestListConfiguredRepos(unittest.TestCase):
#    def setUp(self):
#
#    def test_removes_one_element(self):
