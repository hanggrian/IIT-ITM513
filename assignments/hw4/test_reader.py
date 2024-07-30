"""
Assignment #4
Employee count chart and company profit graphs visualization with Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

import unittest

from reader import read_txt


class TestReader(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(7, len(read_txt('employee_count_by_department.txt', ',')))
        self.assertEqual(10, len(read_txt('last_ten_year_net_profit.txt', ';')))


if __name__ == '__main__':
    unittest.main()
