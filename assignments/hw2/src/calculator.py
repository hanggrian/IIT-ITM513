"""
Assignment #2
Utilize functions declared in a separate file to calculate degrees, radius, and retail cost.

Author: Hendra Wijaya (A20529195)
"""

import math


def r2d(x: float) -> float:
    """Returns the angle of degrees from radians.

    :param x: the radians' angle.
    """
    return x * 180 / math.pi


def d2r(x: float) -> float:
    """Returns the angle of radians from degrees.

    :param x: the degrees' angle.
    """
    return x * math.pi / 180


def get_retail(wholesale: float, markup: float = 2.5) -> float:
    """Returns the retail cost given wholesale price and markup percentage.

    :param wholesale: a positive price.
    :param markup: a positive percentage.
    """
    if wholesale < 0 or markup < 0:
        raise ValueError('The cost or markup cannot be negative.')
    return wholesale * markup


def dollarize(x: float) -> str:
    """Returns the currency string given a number."""
    return '$' + format(x, ',.2f')
