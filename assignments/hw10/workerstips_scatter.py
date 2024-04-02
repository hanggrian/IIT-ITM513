"""
Assignment #10
Graph visualization using Seaborn and Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

from matplotlib import pyplot
from pandas import read_csv
from seaborn import scatterplot

scatterplot(read_csv('workerstips.csv'), x='total_bill', y='tip')
pyplot.show()
