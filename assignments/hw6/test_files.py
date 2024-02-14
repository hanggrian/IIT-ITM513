"""
Assignment #6
Convert LDAP data structure and validate phone numbers using regular expression.

Author: Hendra Wijaya (A20529195)
"""

from re import match
from unittest import TestCase


# pylint: disable=missing-class-docstring, missing-function-docstring
class TestFiles(TestCase):
    def test_ldap(self):
        with open('ldap_input.txt', 'r', encoding='UTF-8') as file:
            for i, line in enumerate(file.read().splitlines()):
                if i == 0:
                    self.assertEqual('#', line[0])
                    continue
                self.assertTrue(match(r'^[a-z]+:[a-zA-Z]+:[a-zA-Z]+:\d{3}-\d{3}-\d{4}$', line))

        with open('ldap_output.txt', 'r', encoding='UTF-8') as file:
            self.assertEqual(4, len(file.read().split('\n\n')))

    def test_phones(self):
        with open('phones_input.txt', 'r', encoding='UTF-8') as file:
            for i, line in enumerate(file.read().splitlines()):
                if i == 0:
                    self.assertEqual('#', line[0])
                    continue
                self.assertTrue(
                    # acceptable
                    match(r'^\d{3}-\d{3}-\d{4}$', line) or
                    match(r'^\(\d{3}\) \d{7}$', line) or
                    match(r'^\(\d{3}\) \d{3} \d{4}$', line) or
                    match(r'^\d{10}$', line) or
                    # invalid format
                    match(r'^\d{3}-\d{4}-\d{3}$', line) or
                    match(r'^\(\d{3}\) \d{3}-\d{4}$', line) or
                    # not 10 digits
                    match(r'^\(\d{3}\) \d{8}$', line) or
                    match(r'^\d{9}$', line),
                )

        with open('phones_output.txt', 'r', encoding='UTF-8') as file:
            self.assertEqual(2, len(file.read().split('\n\n')))
