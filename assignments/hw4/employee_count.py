"""
Assignment #4
Employee count chart and company profit graphs visualization with Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

from matplotlib import pyplot

from reader import read_txt

# pylint: disable=unnecessary-lambda
employees = read_txt(
    'employee_count_by_department.txt',
    ',',
    convert_value=lambda value: int(value),
)

total = sum(employees.values())  # to determine wedge value
pyplot.title('Employees per Department', fontweight='bold')
_, _, autotexts = pyplot.pie(
    list(employees.values()),
    labels=list(employees.keys()),
    autopct=lambda pct: f'{pct:.1f}% ({int(round(pct * total / 100))})',
)
for a in autotexts:
    a.set_size(8)  # to keep label inside wedge
pyplot.show()
