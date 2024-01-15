'''
Assignment #1
Command-line application of polygon area calculator and diesel engine trouble-shooter.

Author: Hendra Wijaya (A20529195)
'''

from src.polygon import get_polygon_area
from src.prompts import prompt_decimal
from src.prompts import prompt_digit

print()

# prompt input
side_count = prompt_digit('Enter the number of sides (3-100): ', 3, 100)
side_length = prompt_decimal('Enter the side (0.1-1000): ', 0.1, 1000.0)

# display result
area = get_polygon_area(side_count, side_length)
print('The area of the polygon is ', '{:.4f}'.format(area))

print()
