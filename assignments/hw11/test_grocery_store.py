"""
Assignment #11
Represent restaurant and grocery store as objects with shared attributes.

Author: Hendra Wijaya (A20529195)
"""

import unittest

from grocery_store import GroceryStore, TYPE_INDEPENDENT
from store import STATUS_OPEN


# pylint: disable=missing-class-docstring, missing-function-docstring
class TestRestaurant(unittest.TestCase):
    def test_constructors(self):
        GroceryStore('Mega Lo Mart', 'Arlen, TX')  # default args
        GroceryStore('Mega Lo Mart', 'Arlen, TX', STATUS_OPEN, 5, TYPE_INDEPENDENT)  # all args

        # invalid parameters
        self.assertRaises(ValueError, GroceryStore, '', '', STATUS_OPEN, 5, TYPE_INDEPENDENT)
        self.assertRaises(ValueError, GroceryStore, 'Mega Lo Mart', 'Arlen, TX', '', -1, '')

    def test_sell_item(self):
        restaurant = GroceryStore('Mega Lo Mart', 'Arlen, TX')
        self.assertEqual(20, restaurant.sell_item(10, 2))
        self.assertEqual(25, restaurant.sell_item(5, 1))

        self.assertRaises(ValueError, GroceryStore.sell_item, GroceryStore, 0, 0)

    def test_calculate(self):
        restaurant = GroceryStore('Mega Lo Mart', 'Arlen, TX')
        self.assertEqual(100, restaurant.sell_item(100, 1))
        self.assertEqual(100, restaurant.calculate_total_sales())
        self.assertEqual(4, int(restaurant.calculate_total_sales_tax()))


if __name__ == '__main__':
    unittest.main()
