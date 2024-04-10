# pylint: disable=invalid-name
"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""

import sys

from calculator import dollarize, get_sales_tax

END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'

prices = []

print()
print(
    f"{BOLD}This program will keep asking for item's price until user enters " +
    f'{UNDERLINE}S{END}{BOLD}top/' +
    f'{UNDERLINE}Q{END}{BOLD}uit{END}',
)
print()


def main():
    """Main recursive function."""
    result = input(f'{YELLOW}Enter the price of item #{len(prices) + 1}: {END}')
    match result.lower():
        case 's' | 'stop':
            return None
        case 'q' | 'quit':
            print()
            print('Goodbye!')
            print()
            sys.exit(0)
    if not result:
        print(f'{RED}Cannot be empty, try again...{END}')
        return main()
    try:
        result = float(result)
    except ValueError:
        print(f'{RED}Parsing error, try again...{END}')
        return main()
    if result < 0:
        print(f'{RED}Invalid negative value, try again...{END}')
        return main()
    prices.append(result)
    return main()


main()

subtotal = 0
print('All items: ', end='')
for p in prices:
    print(dollarize(p), end=' ')
    subtotal += p
print()
print('Subtotal:', f'{GREEN}{dollarize(subtotal)}{END}')

sales_tax = get_sales_tax(subtotal)
print('Sales tax:', f'{GREEN}{dollarize(sales_tax)}{END}')
print('Grand total:', f'{GREEN}{dollarize(subtotal + sales_tax)}{END}')

print()
print('Goodbye!')
print()
