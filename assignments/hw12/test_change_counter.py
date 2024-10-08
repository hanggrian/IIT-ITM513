"""
Assignment #12
Recursion and single-window GUI application wrapped in a main method.

Author: Hendra Wijaya (A20529195)
"""

import unittest

from change_counter import Coin


class TestChangeCounter(unittest.TestCase):
    def test_coin(self):
        self.assertEqual(100, Coin(Coin.DOLLAR, 100).dollar_amount)
        self.assertEqual(25, Coin(Coin.QUARTER, 100).dollar_amount)
        self.assertEqual(10, Coin(Coin.DIME, 100).dollar_amount)
        self.assertEqual(5, Coin(Coin.NICKEL, 100).dollar_amount)
        self.assertEqual(1, Coin(Coin.PENNY, 100).dollar_amount)

        # invalid parameters
        self.assertRaises(ValueError, Coin, Coin.NICKEL, -1)
        self.assertRaises(ValueError, Coin, 'half-dollar', 0)


if __name__ == '__main__':
    unittest.main()
