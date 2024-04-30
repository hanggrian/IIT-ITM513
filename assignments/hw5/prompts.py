"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

Author: Hendra Wijaya (A20529195)
"""

from sys import maxsize

END = '\033[0m'
RED = '\033[31m'


def prompt_text(message: str, allowed_texts: list[str] | None = None) -> str:
    """Recursively ask user for a string value, or allowed text when optional parameter is defined.

    :param message: prompt dialogue.
    :param allowed_texts: set of acceptable text, may be undefined.
    :return: lowercase text.
    """
    result: str = input(f'{message} ').strip()
    if not result:
        return prompt_text(f'{RED}Cannot be empty, try again...{END}', allowed_texts)
    result = result.lower()
    if allowed_texts is None or result in allowed_texts:
        return result
    return prompt_text(f'{RED}Unknown input, try again...{END}', allowed_texts)


def prompt_digit(
    message: str,
    range_from: int = -maxsize - 1,
    range_to: int = maxsize,
) -> int:
    """Recursively ask user for in-bounds digit.

    :param message: prompt dialogue.
    :param range_from: lower bounds.
    :param range_to: upper bounds.
    """
    result: str = input(f'{message} ').strip()
    if not result:
        return prompt_digit(f'{RED}Cannot be empty, try again...{END}', range_from, range_to)
    try:
        result: int = int(result)
        if range_from <= result <= range_to:
            return result
        return prompt_digit(f'{RED}Unknown input, try again...{END}', range_from, range_to)
    except ValueError:
        return prompt_digit(f'{RED}Parsing error, try again...{END}', range_from, range_to)
