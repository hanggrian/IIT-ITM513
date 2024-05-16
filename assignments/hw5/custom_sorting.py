"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

import sys

from matplotlib import pyplot

from prompts import prompt_text
from sorting import timed_sorting

END = '\033[0m'
UNDERLINE = '\033[4m'
YELLOW = '\033[33m'


def bubble_sort(collection):
    """An optimized bubble sort with a swap indicator.
    Modified from https://www.programiz.com/dsa/bubble-sort/.

    :param collection: input data.
    """
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break


def shell_sort(collection):
    """A standard shell sort algorithm.
    Modified from https://www.programiz.com/dsa/shell-sort/.

    :param collection: input data.
    """
    length = len(collection)
    interval = length // 2
    while interval > 0:
        for i in range(interval, length):
            temp = collection[i]
            j = i
            while j >= interval and collection[j - interval] > temp:
                collection[j] = collection[j - interval]
                j -= interval
            collection[j] = temp
        interval //= 2


def _partition(collection, start, end):
    """Rearranges the elements of the subarray between `start` and `end`.

    :param collection: input data.
    :param start: low index.
    :param end: high index (exclusive).
    :return: pivot index.
    """
    pivot = collection[end]
    i = start - 1
    for j in range(start, end):
        if collection[j] <= pivot:
            i += 1
            collection[i], collection[j] = collection[j], collection[i]
    collection[i + 1], collection[end] = collection[end], collection[i + 1]
    return i + 1


def _quicksort(collection, start, end):
    """Recursively sorts a subarray using the quicksort algorithm.

    :param collection: input data
    :param start: low index.
    :param end: high index (exclusive).
    """
    if start < end:
        pivot = _partition(collection, start, end)
        _quicksort(collection, start, pivot - 1)
        _quicksort(collection, pivot + 1, end)


def quicksort(collection) -> None:
    """A standard quicksort algorithm
    Modified from https://www.programiz.com/dsa/quick-sort/.

    :param collection: input data
    """
    _quicksort(collection, 0, len(collection) - 1)


def get_sorting_stats(action):
    """Measures the sorting performance of a given action on different data sizes."""
    return {
        10000: timed_sorting(10000, action),
        30000: timed_sorting(30000, action),
        50000: timed_sorting(50000, action),
        70000: timed_sorting(70000, action),
        90000: timed_sorting(90000, action),
    }


if __name__ == '__main__':
    def apply_axes(axes, title, sort_stats):
        """Configures axes properties before displaying it."""
        axes.set_title(title)
        if sort_stats is not None:
            axes.plot(sort_stats.keys(), sort_stats.values())
        axes.set_xlabel('Range')
        axes.set_ylabel('Time (in seconds)')
        axes.set_xticks(ticks)


    print()
    match (
        prompt_text(
            f'{YELLOW}Do you want to skip bubble_sort for faster result (' +
            f'{UNDERLINE}Y{END}{YELLOW}es/' +
            f'{UNDERLINE}N{END}{YELLOW}o):{END}',
            ['y', 'yes', 'n', 'no', 'q', 'quit'],
        )
    ):
        case 'y' | 'yes':
            bubble_sort_stats: None = None
            shell_sort_stats = get_sorting_stats(shell_sort)
            quicksort_stats = get_sorting_stats(quicksort)
        case 'n' | 'no':
            bubble_sort_stats: dict[int, float] = get_sorting_stats(bubble_sort)
            shell_sort_stats = get_sorting_stats(shell_sort)
            quicksort_stats = get_sorting_stats(quicksort)
        case _:
            print()
            print('Goodbye!')
            print()
            sys.exit(0)

    print('Finished, displaying result.')

    ticks = list(range(10000, 100000, 10000))

    _, ((axes1, axes2), (axes3, axes4)) = pyplot.subplots(2, 2, figsize=(11, 9))
    apply_axes(axes1, 'Bubble Sort Time', bubble_sort_stats)
    apply_axes(axes2, 'Shell Sort Time', shell_sort_stats)
    apply_axes(axes3, 'Quicksort Time', quicksort_stats)
    axes4.set_visible(False)

    pyplot.suptitle('Sorting Statistics', fontweight='bold')
    pyplot.tight_layout()
    pyplot.show()

    print()
    print('Goodbye!')
    print()
