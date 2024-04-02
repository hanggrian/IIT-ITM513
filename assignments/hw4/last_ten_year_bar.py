"""
Assignment #4
Employee count chart and company profit graphs visualization with Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

from matplotlib import pyplot
from price_parser import Price

from reader import read_txt

# pylint: disable=unnecessary-lambda
profits = read_txt(
    'last_ten_year_net_profit.txt',
    ';',
    convert_key=lambda key: int(key),
    convert_value=lambda value: Price.fromstring(value).amount,
)

pyplot.suptitle("Company's Profit Over the Past Ten Years", fontweight='bold')
pyplot.title('Bar Graph')
pyplot.xlabel('Years')
pyplot.ylabel('Net Profit in the 100 millions')
pyplot.bar(list(profits.keys()), list(profits.values()))
pyplot.xticks(list(range(min(profits.keys()), max(profits.keys()) + 1)))
pyplot.show()
