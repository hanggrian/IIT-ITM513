"""
Assignment #1
Command-line application of polygon area calculator and diesel engine troubleshooter.

Author: Hendra Wijaya (A20529195)
"""

from polygon import get_polygon_area
from prompts import prompt_decimal, prompt_digit

END = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[33m'

print()

# prompt input
side_count = prompt_digit(f'{YELLOW}Enter the number of sides (3-100): {END}', 3, 100)
side_length = prompt_decimal(f'{YELLOW}Enter the side (0.1-1000): {END}', 0.1, 1000.0)

# display result
area = get_polygon_area(side_count, side_length)
print(f'The area of the polygon is {BOLD}{area:.4f}{END}')

print()
