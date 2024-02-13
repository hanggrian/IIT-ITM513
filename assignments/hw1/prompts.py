"""
Assignment #1
Command-line application of polygon area calculator and diesel engine troubleshooter.

Author: Hendra Wijaya (A20529195)
"""


def prompt_text(message: str, allowed_texts: list[str]) -> str:
    """Recursively ask user for allowed text.

    :param message: prompt dialogue.
    :param allowed_texts: set of acceptable text.
    :return: lowercase text.
    """
    result: str = input(message).strip()
    if not result:
        return prompt_text('Cannot be empty, try again... ', allowed_texts)
    result = result.lower()
    if result not in allowed_texts:
        return prompt_text('Unknown input, try again... ', allowed_texts)
    return result


def prompt_digit(message: str, range_from: int, range_to: int) -> int:
    """Recursively ask user for in-bounds digit.

    :param message: prompt dialogue.
    :param range_from: lower bounds.
    :param range_to: upper bounds.
    """
    result: str = input(message).strip()
    if not result:
        return prompt_digit('Cannot be empty, try again... ', range_from, range_to)
    try:
        result: int = int(result)
        if range_from <= result <= range_to:
            return result
        return prompt_digit('Unknown input, try again... ', range_from, range_to)
    except ValueError:
        return prompt_digit('Parsing error, try again... ', range_from, range_to)


def prompt_decimal(message: str, range_from: float, range_to: float) -> float:
    """Recursively ask user for in-bounds decimal.

    :param message: prompt dialogue.
    :param range_from: lower bounds.
    :param range_to: upper bounds.
    """
    result: str = input(message)
    if not result:
        return prompt_decimal('Cannot be empty, try again... ', range_from, range_to)
    try:
        result: float = float(result)
        if range_from <= result <= range_to:
            return result
        return prompt_decimal('Unknown input, try again... ', range_from, range_to)
    except ValueError:
        return prompt_decimal('Parsing error, try again... ', range_from, range_to)
