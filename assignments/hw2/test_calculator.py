"""
Assignment #2
Utilize functions declared in a separate file to calculate degrees, radius, and retail cost.

Author: Hendra Wijaya (A20529195)
"""

import math
from unittest import TestCase

from calculator import d2r
from calculator import dollarize
from calculator import get_retail
from calculator import r2d


# pylint: disable=missing-class-docstring, missing-function-docstring
class TestCalculator(TestCase):
    def test_r2d(self):
        self.assertEqual(0, r2d(0))
        self.assertEqual(57, int(r2d(1)))
        self.assertEqual(180, r2d(math.pi))

        # invalid parameter
        self.assertRaises(Exception, r2d, 'foo')

        # compare with built-in
        self.assertEqual(math.degrees(1), r2d(1))
        self.assertEqual(int(math.degrees(math.pi)), int(r2d(math.pi)))

    def test_d2r(self):
        self.assertEqual(0, d2r(0))
        self.assertEqual(1, int(d2r(90)))
        self.assertEqual(math.pi, d2r(180))

        # invalid parameter
        self.assertRaises(Exception, d2r, 'foo')

        # compare with built-in
        self.assertEqual(math.radians(1), d2r(1))
        self.assertEqual(int(math.radians(180)), int(d2r(180)))

    def test_get_retail(self):
        self.assertEqual(0, get_retail(0, 0))
        self.assertEqual(250, get_retail(100, 2.5))

        # invalid parameter
        self.assertRaises(Exception, get_retail, 'foo')
        self.assertRaises(ValueError, get_retail, -1)
        self.assertRaises(ValueError, get_retail, 0, -1)

    def test_dollarize(self):
        self.assertEqual('$0.00', dollarize(0))
        self.assertEqual('$1.23', dollarize(1.23456789))

        # invalid parameter
        self.assertRaises(Exception, dollarize, 'foo')
