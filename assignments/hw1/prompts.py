"""
Assignment #1
Command-line application of polygon area calculator and diesel engine troubleshooter.

Author: Hendra Wijaya (A20529195)
"""

END = '\033[0m'
RED = '\033[31m'


def prompt_text(message: str, allowed_texts: list[str]) -> str:
    """Recursively ask user for allowed text.

    :param message: prompt dialogue.
    :param allowed_texts: set of acceptable text.
    :return: lowercase text.
    """
    result: str = input(f'{message} ').strip()
    if not result:
        return prompt_text(f'{RED}Cannot be empty, try again...{END}', allowed_texts)
    result = result.lower()
    if result not in allowed_texts:
        return prompt_text(f'{RED}Unknown input, try again...{END}', allowed_texts)
    return result


def prompt_digit(message: str, range_from: int, range_to: int) -> int:
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


def prompt_decimal(message: str, range_from: float, range_to: float) -> float:
    """Recursively ask user for in-bounds decimal.

    :param message: prompt dialogue.
    :param range_from: lower bounds.
    :param range_to: upper bounds.
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
