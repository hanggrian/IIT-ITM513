"""
Assignment #1
Command-line application of polygon area calculator and diesel engine troubleshooter.

Author: Hendra Wijaya (A20529195)
"""

from math import tan, pi


def get_polygon_area(sides: int, length: float) -> float:
    """Returns the calculated polygon area.

    :param sides: number of sides.
    :param length: the side length.
    :raises: Exception: when polygon side is below 3 or length is empty.
    """
    if sides < 3 or length == 0:
        raise ValueError('Invalid input.')
    return (sides * length ** 2) / (4 * tan(pi / sides))
