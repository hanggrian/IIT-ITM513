"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

from random import randint
from time import time
from typing import Callable


def generate_random_list(length: int) -> list[int]:
    """Returns a list of randomized numbers.

    :param length: list size and also max random value.
    :return: numbers.
    """
    return [randint(1, length) for _ in range(length)]


def timed_sorting(length: int, action: Callable[[list[int]], None]) -> float:
    """Measure sorting time for a randomly generated list given the action.

    :param length: list size and also max random value.
    :param action: sorting method.
    :return: elapsed time.
    """
    print(f'Timing {action.__name__} of {length} items...')
    initial_time: float = time()
    action(generate_random_list(length))
    return time() - initial_time
