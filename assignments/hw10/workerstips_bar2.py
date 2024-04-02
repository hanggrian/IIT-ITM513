"""
Assignment #10
Graph visualization using Seaborn and Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

from matplotlib import pyplot
from pandas import read_csv
from seaborn import barplot

barplot(read_csv('workerstips.csv'), x='day', y='tip', hue='time')
pyplot.legend(title='time')
pyplot.show()
