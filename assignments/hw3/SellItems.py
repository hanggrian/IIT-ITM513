# pylint: disable=invalid-name
"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""

import sys

from calculator import dollarize
from calculator import get_sales_tax

UNDERLINE = '\033[4m'
BOLD = '\033[1m'
END = '\033[0m'

prices = []

print()
print(
    "This program will keep asking for item's price until user enters " +
    f'{UNDERLINE}S{END}top/' +
    f'{UNDERLINE}Q{END}uit',
)


def main():
    """Main recursive function."""
    result = input(f'Enter the price of item #{len(prices) + 1}: ')
    match result.lower():
        case 's' | 'stop':
            return None
        case 'q' | 'quit':
            print()
            sys.exit(0)
    if not result:
        print('Cannot be empty, try again...')
        return main()
    try:
        result = float(result)
    except ValueError:
        print('Parsing error, try again...')
        return main()
    if result < 0:
        print('Invalid negative value, try again...')
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
print(f'{BOLD}Subtotal: {dollarize(subtotal)}')

sales_tax = get_sales_tax(subtotal)
print(f'Sales tax: {dollarize(sales_tax)}')
print(f'Grand total: {dollarize(subtotal + sales_tax)}')

print()
