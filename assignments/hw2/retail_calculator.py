"""
Assignment #2
Utilize functions declared in a separate file to calculate degrees, radius and retail cost.

Author: Hendra Wijaya (A20529195)
"""

import sys

from calculator import dollarize, get_retail
from prompts import prompt_decimal, prompt_text

END = '\033[0m'
UNDERLINE = '\033[4m'
GREEN = '\033[32m'
YELLOW = '\033[33m'


def main(is_restarting=False):
    """The main recursive function."""
    if is_restarting:
        print('Restarting...')
    print()
    retail = get_retail(prompt_decimal(f"{YELLOW}Enter the item's wholesale cost:{END}", 0))
    print('Retail price:', f'{GREEN}{dollarize(retail)}{END}')
    match prompt_text(
        f'{YELLOW}Do you have another item ({UNDERLINE}Y{END}{YELLOW}es/' +
        f'{UNDERLINE}N{END}{YELLOW}o)?{END}',
        ['y', 'yes', 'n', 'no', 'q', 'quit'],
    ):
        case 'y' | 'yes':
            main(True)
        case _:
            print()
            print('Goodbye!')
            print()
            sys.exit(0)


main()
