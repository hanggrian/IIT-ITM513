"""
Assignment #5
Analyze times spent with sorting methods and display the statistics simultaneously.

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
