"""
Assignment #1
Command-line application of polygon area calculator and diesel engine troubleshooter.

Author: Hendra Wijaya (A20529195)
"""

import sys
from prompts import prompt_digit
from prompts import prompt_text

# input restrictions
COLOR_INPUTS = ['g', 'green', 'a', 'amber', 'r', 'red', 'q', 'quit']
PRESSURE_INPUTS = ['h', 'high', 'n', 'normal', 'l', 'low', 'q', 'quit']
METER_MIN = 0
METER_MAX = 1000


def end():
    """Quit the program."""
    print('Goodbye!')
    print()
    sys.exit(0)


def main(is_restarting=False):
    """Main recursive function."""
    if is_restarting:
        print('Restarting...')
    print()
    print('Check status light.')
    match prompt_text('Color (Green/Amber/Red): ', COLOR_INPUTS):
        case 'g' | 'green':
            print('Do restart procedure.')
            main(True)
        case 'a' | 'amber':
            print('Check fuel line service routine.')
            main(True)
        case 'r' | 'red':
            print('Shut-off al input lines check meter #3.')
            if prompt_digit('Meter (0-1000): ', METER_MIN, METER_MAX) < 50:
                print('Check main line for test pressure.')
                match prompt_text('Pressure (High/Normal/Low): ', PRESSURE_INPUTS):
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
                match prompt_text('Velocity (High/Normal/Low): ', PRESSURE_INPUTS):
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
