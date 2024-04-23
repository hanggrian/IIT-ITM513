"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

from sorting_techniques.pysort import Sorting

from sorting import timed_sorting

LENGTH = 10000

END = '\033[0m'
GREEN = '\033[32m'

sorter = Sorting()

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
print('Fastest sorting:', f'{GREEN}{fastest_time} ({int(stats[fastest_time])} seconds){END}')
print('Slowest sorting:', f'{GREEN}{slowest_time} ({int(stats[slowest_time])} seconds){END}')

print()
print('Goodbye!')
print()
