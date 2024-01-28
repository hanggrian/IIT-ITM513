"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""

import unittest
from src.calculator import get_sales_tax
from src.calculator import dollarize
from src.calculator import multiplyMatrix


class TestCalculator(unittest.TestCase):
    def test_get_sales_tax(self):
        self.assertEqual(0, get_sales_tax(0))
        self.assertEqual(7, int(get_sales_tax(100)))

        # invalid parameter
        self.assertRaises(Exception, get_sales_tax, 'foo')

    def test_dollarize(self):
        self.assertEqual('$0.00', dollarize(0))
        self.assertEqual('$1.23', dollarize(1.23456789))

        # invalid parameter
        self.assertRaises(Exception, dollarize, 'foo')

    def test_multiplyMatrix(self):
        # sample data obtained from https://www.mathsisfun.com/algebra/matrix-multiplying.html
        # 2x2 multiply by 2x2
        matrix = multiplyMatrix([[4, 0], [1, -9]], [[8, 0], [2, -18]])
        self.assertEqual(32, matrix[0][0])
        self.assertEqual(0, matrix[0][1])
        self.assertEqual(-10, matrix[1][0])
        self.assertEqual(162, matrix[1][1])
        # 3x2 multiply by 2x3
        matrix = multiplyMatrix([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
        self.assertEqual(58, matrix[0][0])
        self.assertEqual(64, matrix[0][1])
        self.assertEqual(139, matrix[1][0])
        self.assertEqual(154, matrix[1][1])

        # invalid parameter
        self.assertRaises(ValueError, multiplyMatrix, [[1]], [[1], [1]])
