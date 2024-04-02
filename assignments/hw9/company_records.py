"""
Assignment #9
Command-line application to manage company records in serialization.

Author: Hendra Wijaya (A20529195)
"""

from os.path import isfile
from pickle import load, dump, UnpicklingError

from pandas import DataFrame

from prompts import prompt_text

END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
YELLOW = '\033[33m'

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
    print(f"{UNDERLINE}Enter the number corresponding to what you'd like to do.{END}")
    print()
    print('1. Add a new name and email address.')
    print('2. Find an existing email address from a name.')
    print('3. Change an existing email address.')
    print('4. Delete an existing name and email address.')
    print('5. Export to CSV file.')
    print('6. Exit the program.')
    match prompt_text(f'{YELLOW}Enter a number: {END}', MAIN_OPTIONS):
        case '1':
            name = prompt_text(f'{YELLOW}Enter the name you would like to add: {END}')
            email = prompt_text(f'{YELLOW}Enter the email you would like to add: {END}')
            data[name] = email
            if name not in data:
                print(f'{BOLD}The name and email has been added.{END}')
            else:
                print(f'{BOLD}The name and email has been overridden.{END}')
            main()
        case '2':
            name = prompt_text(
                f'{YELLOW}Enter the name you would like to search: {END}',
                list(data.keys()),
            )
            print(f'{BOLD}The email is: {data[name]}{END}')
            main()
        case '3':
            name = prompt_text(
                f'{YELLOW}Enter the name you would like to change: {END}',
                list(data.keys()),
            )
            email = prompt_text(f'{YELLOW}Enter the email you would like to add: {END}')
            data[name] = email
            print(f'{BOLD}The email has been changed.{END}')
            main()
        case '4':
            name = prompt_text(
                f'{YELLOW}Enter the name you would like to delete: {END}',
                list(data.keys()),
            )
            del data[name]
            print(f'{BOLD}The name and email has been deleted.{END}')
            main()
        case '5':
            file_name = prompt_text(f'{YELLOW}Enter the file name: {END}')
            if not file_name.lower().endswith('.csv'):
                file_name += '.csv'
            DataFrame({
                'Person name': data.keys(),
                'Email address': data.values(),
            }).to_csv(file_name, encoding='UTF-8', index=False)
            print(f"{BOLD}Exporting '{file_name}' file.{END}")
            main()
        case _:
            with open(DATA_FILE, 'wb') as binary_file:  # pylint: disable=redefined-outer-name
                dump(data, binary_file)
            print("Saving 'data' file.")


main()

print()
print('Goodbye!')
print()
