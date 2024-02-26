"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

from sorting_techniques import pysort

from sorting import timed_sorting

LENGTH = 10000

BOLD = '\033[1m'
END = '\033[0m'

sorter = pysort.Sorting()

# skip bogo & stooage for being insanely slow
print()
stats = {
    'Bubble sort': timed_sorting(LENGTH, sorter.bubbleSort),
    'Selection sort': timed_sorting(LENGTH, sorter.selectionSort),
    'Insertion sort': timed_sorting(LENGTH, sorter.insertionSort),
    'Shell sort': timed_sorting(LENGTH, sorter.shellSort),
    'Pigeon hole sort': timed_sorting(LENGTH, sorter.pigeonHoleSort),
    'Heap sort': timed_sorting(LENGTH, sorter.heapSort),
    'Gnome sort': timed_sorting(LENGTH, sorter.gnomeSort),
    # 'Stooage sort': timed_sorting(LENGTH, lambda x: sorter.stoogeSort(x, 0, LENGTH - 1)),
    'Pancake sort': timed_sorting(LENGTH, sorter.pancakeSort),
    # 'Bogo sort': timed_sorting(LENGTH, sorter.bogoSort),
    'Merge sort': timed_sorting(LENGTH, sorter.mergeSort),
    'Quick sort': timed_sorting(LENGTH, lambda x: sorter.quickSort(x, 0, LENGTH - 1)),
    'Cocktail sort': timed_sorting(LENGTH, sorter.cocktailSort),
    'Brick sort': timed_sorting(LENGTH, sorter.brickSort),
    'Radix sort': timed_sorting(LENGTH, sorter.radixSort),
}

fastest_time = min(stats, key=stats.get)
slowest_time = max(stats, key=stats.get)

print()
print(
    f'The fastest is {BOLD}{fastest_time}{END} ' +
    f'running for {BOLD}{int(stats[fastest_time])}{END} seconds.',
)
print(
    f'The slowest is {BOLD}{slowest_time}{END} ' +
    f'running for {BOLD}{int(stats[slowest_time])}{END} seconds.',
)
print('Goodbye!')
print()
