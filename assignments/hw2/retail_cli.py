"""
Assignment #2
Utilize functions declared in a separate file to calculate degrees, radius, and retail cost.

Author: Hendra Wijaya (A20529195)
"""

import sys

from calculator import dollarize
from calculator import get_retail
from prompts import END
from prompts import prompt_decimal
from prompts import prompt_text
from prompts import UNDERLINE


def main(is_restarting=False):
    """Main recursive function."""
    if is_restarting:
        print('Restarting...')
    print()
    retail = get_retail(prompt_decimal("Enter the item's wholesale cost: ", 0))
    print('Retail price: ', dollarize(retail))
    match prompt_text(
        f'Do you have another item ({UNDERLINE}Y{END}es/' +
        f'{UNDERLINE}N{END}o)? ',
        ['y', 'yes', 'n', 'no', 'q', 'quit'],
    ):
        case 'y' | 'yes':
            main(True)
        case _:
            print('Goodbye!')
            print()
            sys.exit(0)


main()
