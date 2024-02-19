"""
Assignment #2
Utilize functions declared in a separate file to calculate degrees, radius and retail cost.

Author: Hendra Wijaya (A20529195)
"""

from calculator import d2r, r2d
from prompts import END, UNDERLINE, prompt_decimal, prompt_text

print()

match prompt_text(
    f'Which angle do you want to convert ({UNDERLINE}D{END}egrees/' +
    f'{UNDERLINE}R{END}adians): ',
    ['d', 'degrees', 'r', 'radians', 'q', 'quit'],
):
    case 'd' | 'degrees':
        radians = d2r(prompt_decimal("Enter the degree's angle: "))
        print(f'The angle of radians is {radians:.4f}')
    case 'r' | 'radians':
        degrees = r2d(prompt_decimal("Enter the radian's angle: "))
        print(f'The angle of degrees is {degrees:.4f}')

print()
