"""
Assignment #8
Pandas library operations and data analysis of Titanic table.

Author: Hendra Wijaya (A20529195)
"""

from numpy.random import randint
from pandas import Series, DataFrame

END = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[32m'

ALPHABETS = 'abcdefghijklmno'

alphabet_counter: int = 0


def print_section(question, answer):
    """Convenient method to answer sub-question."""
    global alphabet_counter  # pylint: disable=invalid-name, global-statement

    print()
    print(f'{ALPHABETS[alphabet_counter]}. {question}')
    print(f'{GREEN}{answer}{END}')

    alphabet_counter = alphabet_counter + 1


print()
print(f'{BOLD}Demonstrating pandas series{END}')

print_section('Create a Series from the list [7, 11, 13, 17].', Series([7, 11, 13, 17]))

print_section('Create a Series with five elements that are all 100.0.', Series(100.0, range(5)))

print_section(
    'Create a Series with 20 elements that are all random numbers in the range 0 to 100.',
    Series(randint(0, 101, 20)).describe(),
)

print_section(
    'Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9.' +
    "Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and " +
    "'Andrea'.",
    Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea']),
)

print_section(
    'Form a dictionary from the names and values in Part (d), then use it to initialize a Series.',
    Series({
        'Julie': 98.6,
        'Charlie': 98.9,
        'Sam': 100.2,
        'Andrea': 97.9,
    }),
)

print()
print(f'{BOLD}Demonstrating pandas dataframes{END}')

# generated randomly using the values in similar range of part (d)
temperature_map = {
    'Maxine': [98.2, 99.8, 102],
    'James': [100.2, 99.0, 97.3],
    'Amanda': [95.6, 94.3, 93.1],
}

print_section(
    'Create a DataFrame named temperatures from a dictionary of three temperature readings each ' +
    "for 'Maxine', 'James' and 'Amanda'.",
    DataFrame(temperature_map),
)

temperature_dataframe = DataFrame(temperature_map, index=['Morning', 'Afternoon', 'Evening'])

print_section(
    'Recreate the DataFrame temperatures in Part (a) with custom indices using the index keyword ' +
    "argument and a list containing 'Morning', 'Afternoon' and 'Evening'.",
    temperature_dataframe,
)

print_section(
    "Select from temperatures the column of temperature readings for 'Maxine'.",
    temperature_dataframe['Maxine'],
)

print_section(
    "Select from temperatures the row of 'Morning' temperature readings.",
    temperature_dataframe.loc['Morning'],
)

print_section(
    "Select from temperatures the rows for 'Morning' and 'Evening' temperature readings.",
    temperature_dataframe.loc[['Morning', 'Evening']],
)

print_section(
    "Select from temperatures the columns of temperature readings for 'Amanda' and 'Maxine'.",
    temperature_dataframe[['Amanda', 'Maxine']],
)

print_section(
    "Select from temperatures the elements for 'Amanda' and 'Maxine' in the 'Morning' and " +
    "'Afternoon'.",
    temperature_dataframe.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']],
)

print_section(
    "Use the describe method to produce temperatures' descriptive statistics.",
    temperature_dataframe.describe(),
)

print_section('Transpose temperatures.', temperature_dataframe.transpose())

print_section(
    'Sort temperatures so that its column names are in alphabetical order.',
    temperature_dataframe.sort_index(axis=1),
)

print()
print('Goodbye!')
print()
