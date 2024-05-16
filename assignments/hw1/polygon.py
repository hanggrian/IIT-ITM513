"""
Assignment #1
Command-line application of polygon area calculator and diesel engine troubleshooter.

Author: Hendra Wijaya (A20529195)
"""

from math import tan, pi

from prompts import prompt_decimal, prompt_digit

END = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'


def get_polygon_area(sides, length):
    """Returns the calculated polygon area.

    :param sides: number of sides.
    :param length: the side length.
    :raises: Exception: when polygon side is below 3 or length is empty.
    """
    if sides < 3 or length == 0:
        raise ValueError('Invalid input.')
    return (sides * length ** 2) / (4 * tan(pi / sides))


if __name__ == '__main__':
    print()

    # prompt input
    side_count = prompt_digit(f'{YELLOW}Enter the number of sides (3-100):{END}', 3, 100)
    side_length = prompt_decimal(f'{YELLOW}Enter the side (0.1-1000):{END}', 0.1, 1000.0)

    # display result
    area = get_polygon_area(side_count, side_length)
    print(f'The area of the polygon is {GREEN}{area:.4f}{END}')

    print()
    print('Goodbye!')
    print()
