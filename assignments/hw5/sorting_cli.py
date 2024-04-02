"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

import sys

from matplotlib import pyplot

from prompts import prompt_text
from sorting import timed_sorting, bubble_sort, shell_sort, quicksort

END = '\033[0m'
UNDERLINE = '\033[4m'
YELLOW = '\033[33m'


def get_sorting_stats(action):
    """Measures the sorting performance of a given action on different data sizes."""
    return {
        10000: timed_sorting(10000, action),
        30000: timed_sorting(30000, action),
        50000: timed_sorting(50000, action),
        70000: timed_sorting(70000, action),
        90000: timed_sorting(90000, action),
    }


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
        f'{YELLOW}Do you want to skip bubble_sort for faster result ' +
        f'({UNDERLINE}Y{END}{YELLOW}es/' +
        f'{UNDERLINE}N{END}{YELLOW}o): {END}',
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
        print('Goodbye!')
        print()
        sys.exit(0)

print('Finished!')
print()

ticks = list(range(10000, 100000, 10000))

_, ((axes1, axes2), (axes3, axes4)) = pyplot.subplots(2, 2, figsize=(11, 9))
apply_axes(axes1, 'Bubble Sort Time', bubble_sort_stats)
apply_axes(axes2, 'Shell Sort Time', shell_sort_stats)
apply_axes(axes3, 'Quicksort Time', quicksort_stats)
axes4.set_visible(False)

pyplot.suptitle('Sorting Statistics', fontweight='bold')
pyplot.tight_layout()
pyplot.show()
