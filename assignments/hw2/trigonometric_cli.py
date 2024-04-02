"""
Assignment #2
Utilize functions declared in a separate file to calculate degrees, radius and retail cost.

Author: Hendra Wijaya (A20529195)
"""

from calculator import d2r, r2d
from prompts import prompt_decimal, prompt_text

END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
YELLOW = '\033[33m'

print()

match prompt_text(
    f'{YELLOW}Which angle do you want to convert ({UNDERLINE}D{END}{YELLOW}egrees/' +
    f'{UNDERLINE}R{END}{YELLOW}adians): {END}',
    ['d', 'degrees', 'r', 'radians', 'q', 'quit'],
):
    case 'd' | 'degrees':
        radians = d2r(prompt_decimal("Enter the degree's angle: "))
        print(f'The angle of radians is {BOLD}{radians:.4f}{END}')
    case 'r' | 'radians':
        degrees = r2d(prompt_decimal("Enter the radian's angle: "))
        print(f'The angle of degrees is {BOLD}{degrees:.4f}{END}')

print()
