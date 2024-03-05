"""
Assignment #8
Pandas library operations and data analysis of Titanic table.

Author: Hendra Wijaya (A20529195)
"""

from pandas import read_csv

BOLD = '\033[1m'
END = '\033[0m'


def get_pronoun(person):
    """Get starting pronunciation of this person."""
    if person['sex'] == 'male':
        return 'He'
    return 'She'


titanic = read_csv('titanic.csv')

print()
print(f'There were {BOLD}{titanic.shape[0]} passengers{END} on the Titanic.')

column_sex = titanic['sex']

print(f"Number of Male Passengers: {BOLD}{titanic[column_sex == 'male'].shape[0]}{END}")
print(f"Number of Female Passengers: {BOLD}{titanic[column_sex == 'female'].shape[0]}{END}")

column_age = titanic['age']

print(f"The average age of all the passengers was {BOLD}{column_age.mean():,.2f}{END}")
print(
    f"There are {BOLD}{titanic[column_age < 21].shape[0]} passengers{END} " +
    'under 21 years old.',
)

column_survived = titanic['survived']
condition_survive = column_survived == 'yes'
condition_deceased = column_survived == 'no'
condition_male = column_sex == 'male'
condition_female = column_sex == 'female'

print(
    f'Total Passengers Survived: {BOLD}{titanic[condition_survive].shape[0]}{END}, ' +
    f'Male: {BOLD}{titanic[condition_survive & condition_male].shape[0]}{END}, ' +
    f'Female: {BOLD}{titanic[condition_survive & condition_female].shape[0]}{END}',
)
print(
    f'Total Passengers Deceased: {BOLD}{titanic[condition_deceased].shape[0]}{END}, ' +
    f'Male: {BOLD}{titanic[condition_deceased & condition_male].shape[0]}{END}, ' +
    f'Female: {BOLD}{titanic[condition_deceased & condition_female].shape[0]}{END}',
)

survivor_youngest = titanic[condition_survive].sort_values(by='age').iloc[0]
survivor_oldest = titanic[condition_survive].sort_values(by='age', ascending=False).iloc[0]

print(
    f"The youngest survivor was {BOLD}{survivor_youngest['Name']}{END}. " +
    f"{get_pronoun(survivor_youngest)} was {BOLD}{survivor_youngest['age']:,.2f}{END} years old.",
)
print(
    f"The oldest survivor was {BOLD}{survivor_oldest['Name']}{END}. " +
    f"{get_pronoun(survivor_oldest)} was {BOLD}{survivor_oldest['age']:,.2f}{END} years old.",
)

print('List of Passengers:')
for name in titanic['Name']:
    print(f'{BOLD}{name}{END}')

print()
print('Goodbye!')
print()
