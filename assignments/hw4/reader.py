"""
Assignment #4
Employee count chart and company profit graphs visualization with Matplotlib.

Author: Hendra Wijaya (A20529195)
"""

import sys
from typing import Any, Callable


def read_txt(
    file_path: str,
    delimiter: str,
    convert_key: Callable[[str], Any] = lambda key: key,
    convert_value: Callable[[str], Any] = lambda value: value,
) -> dict[Any, Any]:
    """Build map from text file, or quit if file is not found.

    :param file_path: file name with extension.
    :param delimiter: text separator for each line.
    :param convert_key: callable to change key type.
    :param convert_value: callable to change value type.
    :return: a map of customized types.
    """
    try:
        result: dict[Any, Any] = {}
        with open(file_path, 'r', encoding='UTF-8') as file:
            for line in file.read().splitlines()[1:]:
                split: list[str] = line.split(delimiter)
                result[convert_key(split[0].strip())] = convert_value(split[1].strip())
        return result
    except FileNotFoundError:
        print('File not found, exiting...')
        sys.exit(1)
