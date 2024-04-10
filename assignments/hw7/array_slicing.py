"""
Assignment #7
Displaying statistics of sliced array and student grading.

Author: Hendra Wijaya (A20529195)
"""

from numpy import arange, reshape

END = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[32m'


def stringify_array(arr):
    """Convert 2-D array into single-line string."""
    return str(arr).replace('\n', ', ')


print()
print(f'{BOLD}Creating{END}')
print()

array = arange(1, 16)

print('Array of 1-15:', f'{GREEN}{array}{END}')

array = reshape(array, (3, 5))

print('Reshaping 3-by-5:', f'{GREEN}{stringify_array(array)}{END}')

print()
print(f'{BOLD}Selecting (index starts at 0){END}')
print()
print('Row 2:', f'{GREEN}{array[2, :]}{END}')
print('Column 4:', f'{GREEN}{array[:, 4]}{END}')
print('Rows 0 & 1:', f'{GREEN}{stringify_array(array[:2, :])}{END}')
print('Columns 2-4:', f'{GREEN}{stringify_array(array[:, 2:(4 + 1)])}{END}')
print('Element in row 1 & column 4:', f'{GREEN}{stringify_array(array[1, 4])}{END}')
print(
    'Elements from row 1 & 2 that are in columns 0, 2 & 4:',
    f'{GREEN}{stringify_array(array[1:(2 + 1), [0, 2, 4]])}{END}',
)

print()
print('Goodbye!')
print()
