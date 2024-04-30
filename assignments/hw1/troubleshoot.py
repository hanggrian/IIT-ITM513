"""
Assignment #1
Command-line application of polygon area calculator and diesel engine troubleshooter.

Author: Hendra Wijaya (A20529195)
"""

import sys

from prompts import prompt_digit, prompt_text

END = '\033[0m'
UNDERLINE = '\033[4m'
YELLOW = '\033[33m'

# input restrictions
COLOR_INPUTS = ['g', 'green', 'a', 'amber', 'r', 'red', 'q', 'quit']
PRESSURE_INPUTS = ['h', 'high', 'n', 'normal', 'l', 'low', 'q', 'quit']
METER_MIN = 0
METER_MAX = 1000


def end():
    """Quit the program."""
    print()
    print('Goodbye!')
    print()
    sys.exit(0)


def main(is_restarting=False):
    """The main recursive function."""
    if is_restarting:
        print('Restarting...')
    print()
    print('Check status light.')
    match prompt_text(
        f'{YELLOW}Color ('
        f'{UNDERLINE}G{END}{YELLOW}reen/' +
        f'{UNDERLINE}A{END}{YELLOW}mber/' +
        f'{UNDERLINE}R{END}{YELLOW}ed):{END}',
        COLOR_INPUTS,
    ):
        case 'g' | 'green':
            print('Do restart procedure.')
            main(True)
        case 'a' | 'amber':
            print('Check fuel line service routine.')
            main(True)
        case 'r' | 'red':
            print('Shut-off al input lines check meter #3.')
            if prompt_digit(f'{YELLOW}Meter (0-1000):{END}', METER_MIN, METER_MAX) < 50:
                print('Check main line for test pressure.')
                match prompt_text(
                    f'{YELLOW}Pressure ('
                    f'{UNDERLINE}H{END}{YELLOW}igh/'
                    f'{UNDERLINE}N{END}{YELLOW}ormal/'
                    f'{UNDERLINE}L{END}{YELLOW}ow):{END}',
                    PRESSURE_INPUTS,
                ):
                    case 'n' | 'normal':
                        print('Refer to motor service manual.')
                        main(True)
                    case 'h' | 'high' | 'l' | 'low':
                        print('Refer to main line manual.')
                        main(True)
                    case _:
                        end()
            else:
                print('Measure flow velocity at inlet 2-B.')
                match prompt_text(
                    f'{YELLOW}Velocity ('
                    f'{UNDERLINE}H{UNDERLINE}{YELLOW}igh/'
                    f'{UNDERLINE}N{END}{YELLOW}ormal/'
                    f'{UNDERLINE}L{END}{YELLOW}ow):{END}',
                    PRESSURE_INPUTS,
                ):
                    case 'n' | 'normal':
                        print('Refer to inlet service manual.')
                        main(True)
                    case 'h' | 'high' | 'l' | 'low':
                        print('Refer unit for factory service.')
                        main(True)
                    case _:
                        end()
        case _:
            end()


main()
