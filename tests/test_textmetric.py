#!/usr/bin/env python

"""
test_textmetric
-----------------

Tests for the `textmetric` module.
"""

import unittest

from textmetric.density import ttr


class TestTextmetric(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_ttr(self):
        with self.assertRaises(ValueError):
            ttr.measure('')

    def test_001_ttr(self):
        self.assertEqual(ttr.measure('A'), 1.0)

    def test_002_ttr(self):
        self.assertEqual(ttr.measure('A A'), 0.5)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
