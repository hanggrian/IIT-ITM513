'''
Assignment #1
Command-line application of polygon area calculator and diesel engine trouble-shooter.

Author: Hendra Wijaya (A20529195)
'''

import math


def get_polygon_area(n: int, s: float) -> float:
    """Returns the calculated polygon area.

    :param n: number of sides
    :param s: the side length
    :raises: Exception: when polygon side is below 3 or length is empty.
    """
    if n < 3 or s == 0:
        raise Exception('Invalid input.')
    return (n * s ** 2) / (4 * math.tan(math.pi / n))
