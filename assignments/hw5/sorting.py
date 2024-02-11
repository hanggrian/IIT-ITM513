"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

from random import randint
from time import time
from typing import Callable


def generate_random_list(length: int) -> list[int]:
    """Returns a list of randomized numbers.

    :param length: list size and also max random value.
    :return: numbers.
    """
    return [randint(1, length) for _ in range(length)]


def timed_sorting(length: int, action: Callable[[list[int]], None]) -> float:
    """Measure sorting time for a randomly generated list given the action.

    :param length: list size and also max random value.
    :param action: sorting method.
    :return: elapsed time.
    """
    print(f'Timing {action.__name__} of {length} items...')
    initial_time = time()
    action(generate_random_list(length))
    surpassed_time = time() - initial_time
    return surpassed_time


def bubble_sort(collection: list[int]) -> None:
    """An optimized bubble sort with a swap indicator.
    Modified from https://www.programiz.com/dsa/bubble-sort/.

    :param collection: input data.
    """
    length: int = len(collection)
    for i in range(length):
        swapped: bool = False
        for j in range(0, length - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break


def shell_sort(collection: list[int]) -> None:
    """A standard shell sort algorithm.
    Modified from https://www.programiz.com/dsa/shell-sort/.

    :param collection: input data.
    """
    length: int = len(collection)
    interval: int = length // 2
    while interval > 0:
        for i in range(interval, length):
            temp: int = collection[i]
            j: int = i
            while j >= interval and collection[j - interval] > temp:
                collection[j] = collection[j - interval]
                j -= interval
            collection[j] = temp
        interval //= 2


def _partition(collection: list[int], start: int, end: int) -> int:
    """Rearranges the elements of the subarray between `start` and `end`.

    :param collection: input data.
    :param start: low index.
    :param end: high index (exclusive).
    :return: pivot index.
    """
    pivot: int = collection[end]
    i: int = start - 1
    for j in range(start, end):
        if collection[j] <= pivot:
            i += 1
            collection[i], collection[j] = collection[j], collection[i]
    collection[i + 1], collection[end] = collection[end], collection[i + 1]
    return i + 1


def _quicksort(collection: list[int], start: int, end: int) -> None:
    """Recursively sorts a subarray using the quicksort algorithm.

    :param collection: input data
    :param start: low index.
    :param end: high index (exclusive).
    """
    if start < end:
        pivot: int = _partition(collection, start, end)
        _quicksort(collection, start, pivot - 1)
        _quicksort(collection, pivot + 1, end)


def quicksort(collection: list[int]) -> None:
    """A standard quicksort algorithm
    Modified from https://www.programiz.com/dsa/quick-sort/.

    :param collection: input data
    """
    _quicksort(collection, 0, len(collection) - 1)
