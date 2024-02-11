"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

import sys

from matplotlib import pyplot

from prompts import prompt_text
from sorting import timed_sorting, bubble_sort, shell_sort, quicksort

UNDERLINE: str = '\033[4m'
END: str = '\033[0m'


def get_sorting_stats(action):
    """Measures the sorting performance of a given action on different data sizes."""
    return {
        10000: timed_sorting(10000, action),
        30000: timed_sorting(30000, action),
        50000: timed_sorting(50000, action),
        70000: timed_sorting(70000, action),
        90000: timed_sorting(90000, action),
    }


def display_axes(axes, title):
    """Configures axes properties before displaying it."""
    axes.set_title(title)
    axes.set_xlabel('Range')
    axes.set_ylabel('Time (in seconds)')
    axes.set_xticks(ticks)


print()
match (
    prompt_text(
        'Do you want to skip bubble_sort for faster result ' +
        f'({UNDERLINE}Y{END}es/{UNDERLINE}N{END}o): ',
        ['y', 'yes', 'n', 'no', 'q', 'quit'],
    )
):
    case 'y' | 'yes':
        bubble_sort_stats = None  # pylint: disable=invalid-name
        shell_sort_stats = get_sorting_stats(shell_sort)
        quicksort_stats = get_sorting_stats(quicksort)
    case 'n' | 'no':
        bubble_sort_stats = get_sorting_stats(bubble_sort)
        shell_sort_stats = get_sorting_stats(shell_sort)
        quicksort_stats = get_sorting_stats(quicksort)
    case _:
        print('Goodbye!')
        print()
        sys.exit(0)

print('Finished!')
print()

ticks = list(range(10000, 100000, 10000))

_, ((axes1, axes2), (axes3, axes4)) = pyplot.subplots(2, 2, figsize=(11, 9))
if bubble_sort_stats is not None:
    axes1.plot(bubble_sort_stats.keys(), bubble_sort_stats.values())
axes2.plot(shell_sort_stats.keys(), shell_sort_stats.values())
axes3.plot(quicksort_stats.keys(), quicksort_stats.values())

display_axes(axes1, 'Bubble Sort Time')
display_axes(axes2, 'Shell Sort Time')
display_axes(axes3, 'Quicksort Time')
axes4.set_visible(False)

pyplot.suptitle('Sorting Statistics', fontweight='bold')
pyplot.tight_layout()
pyplot.show()
