"""
Assignment #12
Recursion and single-window GUI application wrapped in a main method.

Author: Hendra Wijaya (A20529195)
"""

END = '\033[0m'
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'


def does_password_pass_check(password):
    """
    Returns true when password contains at least one digit character.

    :param password: text to check.
    :return: pass condition.
    """
    if len(password) == 0:
        return False
    if password[0].isdigit():
        return True
    return does_password_pass_check(password[1:])


def print_example(password):
    """
    Output an entry into CLI showing validity of input password

    :param password: text to check.
    """
    example = does_password_pass_check(password)
    if example:
        color = GREEN
    else:
        color = RED
    print('Example:', f'{color}{password}{END}')


def main():
    """The main function."""
    print()
    print(f'{BOLD}Pro tip: Include at least one digit in your password{END}')
    print()
    print('If your password contains only text, convert it to a number equivalent.')
    print_example('trick')
    print_example('Tr1Ck')
    print_example('basketball')
    print_example('84sk37b4LL')
    print()
    print('While strong passwords are encouraged, they do not pass the check without a digit.')
    print_example('coW!burN#movE?pianOh')
    print_example('IwiCcR!fOdIiNkE?')
    print()
    print('Goodbye!')
    print()


if __name__ == "__main__":
    main()
