"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

from unittest import TestCase

from sorting import generate_random_list, bubble_sort, shell_sort, quicksort


# pylint: disable=missing-class-docstring, missing-function-docstring, invalid-name
class TestSorting(TestCase):
    def assertSorted(self, collection):
        """Makes sure that every sorting method is appropriate."""
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                raise AssertionError('Sorting method is flawed.')

    def test_bubble_sort(self):
        collection = generate_random_list(1000)
        bubble_sort(collection)
        self.assertSorted(collection)

    def test_shell_sort(self):
        collection = generate_random_list(1000)
        shell_sort(collection)
        self.assertSorted(collection)

    def test_quicksort(self):
        collection = generate_random_list(1000)
        quicksort(collection)
        self.assertSorted(collection)
