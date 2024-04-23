"""
Assignment #13
California pair plots and regression model in New York temperature scatter plot.

Author: Hendra Wijaya (A20529195)
"""

from matplotlib import pyplot
from pandas import DataFrame
from seaborn import pairplot
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
df = DataFrame(housing.data, columns=housing.feature_names)  # pylint: disable=no-member

pairplot(df)
pyplot.show()
