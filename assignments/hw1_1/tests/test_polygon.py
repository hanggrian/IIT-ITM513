'''
Assignment #1
Command-line application of polygon area calculator and diesel engine trouble-shooter.

Author: Hendra Wijaya (A20529195)
'''

import unittest
from src.polygon import get_polygon_area


class TestPolygon(unittest.TestCase):
    def test_get_polygon_area(self):
        self.assertEqual(72, int(get_polygon_area(5, 6.5)))
        self.assertEqual(0, int(get_polygon_area(3, 1)))

        self.assertRaises(Exception, get_polygon_area, 2, 1)
        self.assertRaises(Exception, get_polygon_area, 3, 0)
