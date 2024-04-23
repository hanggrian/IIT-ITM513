"""
Assignment #13
California pair plots and regression model in New York temperature scatter plot.

Author: Hendra Wijaya (A20529195)
"""

from matplotlib import pyplot
from pandas import read_csv
from sklearn.linear_model import LinearRegression

temperature = read_csv('ave_yearly_temp_nyc_1895-2017.csv')

date = temperature['Date'] // 100
value = temperature['Value']

x = date.values.reshape(-1, 1)
y = value.values

model = LinearRegression()
model.fit(x, y)

pyplot.scatter(date, value, label='Original')
pyplot.plot(date, model.predict(x), color='red', label='Regressed')
pyplot.grid(True)
pyplot.xlabel('Year')
pyplot.ylabel('Average Yearly Temperature (°F)')
pyplot.title('Average Yearly Temperature Trend in NYC (1895-2017)')
pyplot.legend()
pyplot.show()
