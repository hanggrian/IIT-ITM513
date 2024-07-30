# pylint: disable=invalid-name
"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""

import unittest

from MultiplyMatrices import multiplyMatrix


class TestMultiplyMatrices(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
