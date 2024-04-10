"""
Assignment #8
Pandas library operations and data analysis of Titanic table.

Author: Hendra Wijaya (A20529195)
"""

from pandas import read_csv

END = '\033[0m'
GREEN = '\033[32m'


def get_pronoun(person):
    """Get starting pronunciation of this person."""
    if person['sex'] == 'male':
        return 'He'
    return 'She'


titanic = read_csv('titanic.csv')

print()
print(f'There were {GREEN}{titanic.shape[0]} passengers{END} on the Titanic.')

series_sex = titanic['sex']

print('Number of Male Passengers:', f"{GREEN}{titanic[series_sex == 'male'].shape[0]}{END}")
print('Number of Female Passengers:', f"{GREEN}{titanic[series_sex == 'female'].shape[0]}{END}")

series_age = titanic['age']

print(f'The average age of all the passengers was {GREEN}{series_age.mean():,.2f}{END}')
print(f'There are {GREEN}{titanic[series_age < 21].shape[0]} passengers {END} under 21 years old.')

series_survived = titanic['survived']
condition_survive = series_survived == 'yes'
condition_deceased = series_survived == 'no'
condition_male = series_sex == 'male'
condition_female = series_sex == 'female'

print(
    'Total Passengers Survived:',
    f'{GREEN}{titanic[condition_survive].shape[0]}{END}, ',
    'Male:',
    f'{GREEN}{titanic[condition_survive & condition_male].shape[0]}{END}, ',
    'Female:',
    f'{GREEN}{titanic[condition_survive & condition_female].shape[0]}{END}',
)
print(
    'Total Passengers Deceased:',
    f'{GREEN}{titanic[condition_deceased].shape[0]}{END}, ',
    'Male:',
    f'{GREEN}{titanic[condition_deceased & condition_male].shape[0]}{END}, ',
    'Female:',
    f'{GREEN}{titanic[condition_deceased & condition_female].shape[0]}{END}',
)

survivor_youngest = titanic[condition_survive].sort_values(by='age').iloc[0]
survivor_oldest = titanic[condition_survive].sort_values(by='age', ascending=False).iloc[0]

print(
    f"The youngest survivor was {GREEN}{survivor_youngest['Name']}. {END}" +
    f"{get_pronoun(survivor_youngest)} was {GREEN}{survivor_youngest['age']:,.2f}{END} years old.",
)
print(
    f"The oldest survivor was {GREEN}{survivor_oldest['Name']}. {END}" +
    f"{get_pronoun(survivor_oldest)} was {GREEN}{survivor_oldest['age']:,.2f}{END} years old.",
)

print('List of Passengers:')
for name in titanic['Name']:
    print(f'{GREEN}{name}{END}')

print()
print('Goodbye!')
print()
