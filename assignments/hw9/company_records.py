"""
Assignment #9
Command-line application to manage company records in serialization.

Author: Hendra Wijaya (A20529195)
"""

from os.path import isfile
from pickle import load, dump, UnpicklingError

from pandas import DataFrame

from prompts import prompt_text

MAIN_OPTIONS = ['1', '2', '3', '4', '5', '6', 'q']
DATA_FILE = 'data.pkl'

# map of person name to email address
data: dict[str, str]

print()
if not isfile(DATA_FILE):
    data = {}
    print("A 'data' file was created.")
else:
    with open(DATA_FILE, 'rb') as binary_file:
        try:
            data = load(binary_file)
            print("An existing 'data' file is found.")
        except UnpicklingError:
            data = {}
            print("An existing 'data' file was corrupted.")


def main():
    """Recursive function until user enters 'Q' key or explicitly exits."""
    print()
    print("Enter the number corresponding to what you'd like to do.")
    print()
    print('1. Add a new name and email address.')
    print('2. Find an existing email address from a name.')
    print('3. Change an existing email address.')
    print('4. Delete an existing name and email address.')
    print('5. Export to CSV file.')
    print('6. Exit the program.')
    match prompt_text('Enter a number: ', MAIN_OPTIONS):
        case '1':
            name = prompt_text('Enter the name you would like to add: ')
            email = prompt_text('Enter the email you would like to add: ')
            data[name] = email
            if name not in data:
                print('The name and email has been added.')
            else:
                print('The name and email has been overridden.')
            main()
        case '2':
            name = prompt_text('Enter the name you would like to search: ', list(data.keys()))
            print(f'The email is: {data[name]}')
            main()
        case '3':
            name = prompt_text('Enter the name you would like to change: ', list(data.keys()))
            email = prompt_text('Enter the email you would like to add: ')
            data[name] = email
            print('The email has been changed.')
            main()
        case '4':
            name = prompt_text('Enter the name you would like to delete: ', list(data.keys()))
            del data[name]
            print('The name and email has been deleted.')
            main()
        case '5':
            file_name = prompt_text('Enter the file name: ')
            if not file_name.lower().endswith('.csv'):
                file_name += '.csv'
            DataFrame({
                'Person name': data.keys(),
                'Email address': data.values(),
            }).to_csv(file_name, encoding='UTF-8', index=False)
            print(f"Exporting '{file_name}' file.")
            main()
        case _:
            with open(DATA_FILE, 'wb') as binary_file:  # pylint: disable=redefined-outer-name
                dump(data, binary_file)
            print("Saving 'data' file.")


main()

print()
print('Goodbye!')
print()
