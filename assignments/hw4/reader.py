"""
Assignment #4
Employee count chart and company profit graphs visualization with Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

import sys
from typing import Any
from typing import Callable


def read_file(
    file_name: str,
    delimiter: str,
    convert_key: Callable[[str], Any] = lambda value: value,
    convert_value: Callable[[str], Any] = lambda value: value,
):
    """Build map from text file, or quit if file is not found.

    :param file_name: text file name without extension.
    :param delimiter: text separator for each line.
    :param convert_key: callable to change key type.
    :param convert_value: callable to change value type.
    :return:
    """
    try:
        result = {}
        with open(f'{file_name}.txt', 'r', encoding='UTF-8') as file:
            for line in file.read().splitlines()[1:]:
                split = line.split(delimiter)
                result[convert_key(split[0].strip())] = convert_value(split[1].strip())
        return result
    except FileNotFoundError:
        print('File not found, exiting...')
        sys.exit(1)
