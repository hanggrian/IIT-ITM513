"""
Assignment #7
Displaying statistics of sliced array and student grading.

Author: Hendra Wijaya (A20529195)
"""

from numpy import arange, reshape

BOLD = '\033[1m'
END = '\033[0m'


def stringify_array(arr):
    """Convert 2-D array into single-line string."""
    return str(arr).replace('\n', ', ')


print()
print('Creating...')

array = arange(1, 16)

print(f'Array of 1-15: {BOLD}{array}{END}')

array = reshape(array, (3, 5))

print(f'Reshaping 3-by-5: {BOLD}{stringify_array(array)}{END}')

print()
print('Selecting (index starts at 0)...')
print(f'Row 2: {BOLD}{array[2, :]}{END}')
print(f'Column 4: {BOLD}{array[:, 4]}{END}')
print(f'Rows 0 & 1: {BOLD}{stringify_array(array[:2, :])}{END}')
print(f'Columns 2-4: {BOLD}{stringify_array(array[:, 2:(4 + 1)])}{END}')
print(f'Element in row 1 & column 4: {BOLD}{stringify_array(array[1, 4])}{END}')
print(
    'Elements from row 1 & 2 that are in columns 0, 2 & 4: ' +
    f'{BOLD}{stringify_array(array[1:(2 + 1), [0, 2, 4]])}{END}',
)

print()
print('Goodbye!')
print()
