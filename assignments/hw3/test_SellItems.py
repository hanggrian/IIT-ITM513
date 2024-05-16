# pylint: disable=invalid-name
"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""

import unittest

from SellItems import get_sales_tax


# pylint: disable=missing-class-docstring, missing-function-docstring
class TestSellItems(unittest.TestCase):
    def test_get_sales_tax(self):
        self.assertEqual(0, get_sales_tax(0))
        self.assertEqual(7, int(get_sales_tax(100)))

        # invalid parameter
        self.assertRaises(Exception, get_sales_tax, 'foo')


if __name__ == '__main__':
    unittest.main()
