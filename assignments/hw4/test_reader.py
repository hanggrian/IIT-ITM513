"""
Assignment #4
Employee count chart and company profit graphs visualization with Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

from unittest import TestCase

from reader import read_file


# pylint: disable=missing-class-docstring, missing-function-docstring
class TestReader(TestCase):
    def test_read_file(self):
        self.assertEqual(7, len(read_file('employee_count_by_department', ',')))
        self.assertEqual(10, len(read_file('last_ten_year_net_profit', ';')))
