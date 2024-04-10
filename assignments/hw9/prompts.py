"""
Assignment #9
Command-line application to manage company records in serialization.

Author: Hendra Wijaya (A20529195)
"""

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
