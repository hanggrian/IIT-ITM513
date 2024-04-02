"""
Assignment #7
Displaying statistics of sliced array and student grading.

Author: Hendra Wijaya (A20529195)
"""

import numpy
from matplotlib import pyplot
from pandas import read_csv
from scipy.stats import mode

END = '\033[0m'
BOLD = '\033[1m'

array = read_csv('student_grades.csv').to_numpy()

print()
print('Display data')
print(f'{BOLD}{array}{END}')

print()
print(f'There are {BOLD}{array.shape[0]}{END} students')

print()
print('Display numbers of rows and columns')
print(f'{BOLD}({array.shape[0]}, {array.shape[1]}){END}')

print()
print('Display data type')
print(f'{BOLD}{array.dtype}{END}')

print()
print('Descriptive Statistics ...')

# basis of statistics and pie chart
overalls = array[:, 31]

print(f'\tMin overall score: {BOLD}{min(overalls)}{END}')
print(f'\tMax overall score: {BOLD}{max(overalls)}{END}')
print(f'\tMean: {BOLD}{numpy.mean(overalls)}{END}')
print(f'\tMedian: {BOLD}{numpy.median(overalls)}{END}')
print(f'\tMode: {BOLD}{mode(overalls)[0]}{END}')
print(f'\tStd. Dev.: {BOLD}{numpy.std(overalls)}{END}')
print(
    '\tPercentile (25%, 75%): ' +
    f'{BOLD}[{numpy.percentile(overalls, 25)} {numpy.percentile(overalls, 75)}]{END}',
)

# gradually receding 10 points on each level until F
grades = {
    'A': sum((90 <= overalls) & (overalls <= 100)),
    'B': sum((80 <= overalls) & (overalls < 90)),
    'C': sum((70 <= overalls) & (overalls < 80)),
    'D': sum((60 <= overalls) & (overalls < 70)),
    'F': sum(overalls < 60),
}

print()
print('Number of students achieved in each grade category:')
print(f"{BOLD}{grades['A']}{END} A")
print(f"{BOLD}{grades['B']}{END} B")
print(f"{BOLD}{grades['C']}{END} C")
print(f"{BOLD}{grades['D']}{END} D")
print(f"{BOLD}{grades['F']}{END} F")

# draw pie chart
pyplot.title('Student Performance Pie Chart', fontweight='bold')
_, _, autotexts = pyplot.pie(
    list(grades.values()),
    labels=[e + ' std' for e in grades],
    autopct=lambda pct: f'{pct:.1f}%',
)
for a in autotexts:
    a.set_size(8)  # to keep label inside wedge
pyplot.show()

print()
print('Goodbye!')
print()
