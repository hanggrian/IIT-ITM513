"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

from sorting_techniques.pysort import Sorting

from prompts import prompt_digit
from sorting import timed_sorting

END = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'

# ask for user input
print()
length = prompt_digit(f'{YELLOW}Insert the number of items to test:{END}', range_from=2)

# skip bogo & stooage for being insanely slow
print()
sorter = Sorting()
stats = {
    'Bubble sort': timed_sorting(length, sorter.bubbleSort),
    'Selection sort': timed_sorting(length, sorter.selectionSort),
    'Insertion sort': timed_sorting(length, sorter.insertionSort),
    'Shell sort': timed_sorting(length, sorter.shellSort),
    'Pigeon hole sort': timed_sorting(length, sorter.pigeonHoleSort),
    'Heap sort': timed_sorting(length, sorter.heapSort),
    'Gnome sort': timed_sorting(length, sorter.gnomeSort),
    # 'Stooage sort': timed_sorting(LENGTH, lambda x: sorter.stoogeSort(x, 0, LENGTH - 1)),
    'Pancake sort': timed_sorting(length, sorter.pancakeSort),
    # 'Bogo sort': timed_sorting(LENGTH, sorter.bogoSort),
    'Merge sort': timed_sorting(length, sorter.mergeSort),
    'Quick sort': timed_sorting(length, lambda x: sorter.quickSort(x, 0, length - 1)),
    'Cocktail sort': timed_sorting(length, sorter.cocktailSort),
    'Brick sort': timed_sorting(length, sorter.brickSort),
    'Radix sort': timed_sorting(length, sorter.radixSort),
}

fastest_time = min(stats, key=stats.get)
slowest_time = max(stats, key=stats.get)
print('Fastest sorting:', f'{GREEN}{fastest_time} ({int(stats[fastest_time])} seconds){END}')
print('Slowest sorting:', f'{GREEN}{slowest_time} ({int(stats[slowest_time])} seconds){END}')

print()
print('Goodbye!')
print()
