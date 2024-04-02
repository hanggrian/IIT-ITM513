"""
Assignment #10
Graph visualization using Seaborn and Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

from warnings import simplefilter

from matplotlib import pyplot
from pandas import read_csv
from seaborn import lineplot

BOLD = '\033[1m'
END = '\033[0m'

simplefilter(action='ignore', category=FutureWarning)

avg_passengers = (
    read_csv('flight_data.csv')
    .groupby(['year', 'month'])['passengers']
    .mean()
    .reset_index()
)
max_annual_passengers = avg_passengers.groupby('year')['passengers'].sum().reset_index()

print()
print(f"Total number of passengers per year are\n{BOLD}${max_annual_passengers}{END}")
print()
print('Goodbye!')
print()

lineplot(
    avg_passengers,
    x='year',
    y='passengers',
    hue='month',
    style='month',
)
pyplot.show()
