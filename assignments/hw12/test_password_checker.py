"""
Assignment #12
Recursion and single-window GUI application wrapped in a main method.

Author: Hendra Wijaya (A20529195)
"""

import unittest

from password_checker import does_password_pass_check


class TestPasswordChecker(unittest.TestCase):
    def test_password_checker(self):
        self.assertTrue(does_password_pass_check('1234'))
        self.assertTrue(does_password_pass_check('ABC123'))
        self.assertTrue(does_password_pass_check('pass1'))

        # invalid parameters
        self.assertFalse(does_password_pass_check(''))
        self.assertFalse(does_password_pass_check('password'))
        self.assertFalse(does_password_pass_check('!@#$%^&*'))


if __name__ == '__main__':
    unittest.main()
