"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

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
