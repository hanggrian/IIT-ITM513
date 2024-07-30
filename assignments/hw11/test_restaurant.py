"""
Assignment #11
Represent restaurant and grocery store as objects with shared attributes.

Author: Hendra Wijaya (A20529195)
"""

import unittest

from restaurant import Restaurant
from store import STATUS_OPEN


class TestRestaurant(unittest.TestCase):
    def test_constructors(self):
        Restaurant('Casa Bonita', 'Lakewood, CO', 10, 2)  # default args
        Restaurant('Casa Bonita', 'Lakewood, CO', 10, 2, STATUS_OPEN, 5)  # all args

        # invalid parameters
        self.assertRaises(ValueError, Restaurant, 'Casa Bonita', '', 10, 2, STATUS_OPEN, 5)
        self.assertRaises(ValueError, Restaurant, 'Casa Bonita', 'Lakewood, CO', 10, 2, '', -1)

    def test_seat_patrons(self):
        restaurant = Restaurant('Casa Bonita', 'Lakewood, CO', 10, 2)
        self.assertFalse(restaurant.seat_patrons(15))  # exceeds limit
        self.assertTrue(restaurant.seat_patrons(5))
        self.assertEqual(5, restaurant.current_occupancy)

        self.assertRaises(ValueError, Restaurant.seat_patrons, Restaurant, 0)

    def test_serve_patrons(self):
        restaurant = Restaurant('Casa Bonita', 'Lakewood, CO', 10, 2)
        self.assertTrue(restaurant.seat_patrons(5))
        self.assertEqual(5, restaurant.serve_patrons(10))  # adjusted to limit

        self.assertRaises(ValueError, Restaurant.seat_patrons, Restaurant, 0)

    def test_checkout_patrons(self):
        restaurant = Restaurant('Casa Bonita', 'Lakewood, CO', 10, 2)
        self.assertTrue(restaurant.seat_patrons(10))
        self.assertEqual(10, restaurant.serve_patrons(10))
        self.assertEqual(0, restaurant.checkout_patrons(15))  # adjusted to limit

        self.assertRaises(ValueError, Restaurant.seat_patrons, Restaurant, 0)

    def test_calculate(self):
        restaurant = Restaurant('Casa Bonita', 'Lakewood, CO', 10, 2)
        self.assertTrue(restaurant.seat_patrons(10))
        self.assertEqual(10, restaurant.serve_patrons(10))
        self.assertEqual(0, restaurant.checkout_patrons(10))
        self.assertEqual(20, restaurant.calculate_total_sales())
        self.assertEqual(1, int(restaurant.calculate_total_sales_tax()))


if __name__ == '__main__':
    unittest.main()
