"""
Assignment #10
Graph visualization using Seaborn and Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

from matplotlib import pyplot
from pandas import read_csv
from seaborn import barplot

END = '\033[0m'
GREEN = '\033[32m'

avg_daily_tip = read_csv('workerstips.csv').groupby('day')['tip'].mean().reset_index()
max_tip = avg_daily_tip.loc[avg_daily_tip['tip'].idxmax()]

print()
print(f"{max_tip['day']} is the highest average tip day at {GREEN}${max_tip['tip']:.2f}.{END}")
print()
print('Goodbye!')
print()

barplot(avg_daily_tip, x='day', y='tip')
pyplot.show()
