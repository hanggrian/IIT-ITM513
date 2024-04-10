"""
Assignment #2
Utilize functions declared in a separate file to calculate degrees, radius and retail cost.

Author: Hendra Wijaya (A20529195)
"""

from sys import float_info

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


def prompt_decimal(
    message: str,
    range_from: float = -float_info.min,
    range_to: float = float_info.max,
) -> float:
    """Recursively ask user for a decimal value, or in-bounds value when optional parameters are
    defined.

    :param message: prompt dialogue.
    :param range_from: lower bounds, may be undefined.
    :param range_to: upper bounds, may be undefined.
    """
    result: str = input(f'{message} ').strip()
    if not result:
        return prompt_decimal(f'{RED}Cannot be empty, try again...{END}', range_from, range_to)
    try:
        result: float = float(result)
        if range_from <= result <= range_to:
            return result
        return prompt_decimal(f'{RED}Unknown input, try again...{END}', range_from, range_to)
    except ValueError:
        return prompt_decimal(f'{RED}Parsing error, try again...{END}', range_from, range_to)
