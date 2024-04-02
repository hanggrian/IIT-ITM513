"""
Assignment #10
Graph visualization using Seaborn and Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

from matplotlib import pyplot
from pandas import read_csv
from seaborn import barplot


def apply_axes(axes, title, data):
    """Configures axes properties before displaying it."""
    axes.set_title(title)
    inner_axes = barplot(x=data.index, y=data.values, ax=axes)
    inner_axes.set(xlabel=None)  # replaced by global label


titanic = read_csv('titanic.csv')
series_sex = titanic['Sex']
series_survive = titanic['Survived']

titanic['class'] = titanic['Pclass'].map({1: 'First', 2: 'Second', 3: 'Third'})
passengers_deceased = titanic[series_survive == 0]['class'].value_counts().sort_index()
passengers_survived = titanic[series_survive == 1]['class'].value_counts().sort_index()

figure, (axes1, axes2) = pyplot.subplots(1, 2)
apply_axes(axes1, 'survived = 0', passengers_deceased)
apply_axes(axes2, 'survived = 1', passengers_survived)

figure.supylabel('count')
figure.supxlabel('class')
pyplot.show()
