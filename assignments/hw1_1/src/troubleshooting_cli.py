'''
Assignment #1
Command-line application of polygon area calculator and diesel engine trouble-shooter.

Author: Hendra Wijaya (A20529195)
'''

from prompts import prompt_digit
from prompts import prompt_text

# input restrictions
COLOR_INPUTS = ['g', 'green', 'a', 'amber', 'r', 'red', 'q', 'quit']
PRESSURE_INPUTS = ['h', 'high', 'n', 'normal', 'l', 'low', 'q', 'quit']
METER_MIN = 0
METER_MAX = 1000


def goodbye():
    print('Goodbye!')
    exit(0)


def troubleshoot(is_restarting=False):
    if is_restarting:
        print('Restarting...')
    print()
    print('Check status light.')
    match prompt_text('Color (Green/Amber/Red): ', COLOR_INPUTS):
        case 'g' | 'green':
            print('Do restart procedure.')
            troubleshoot(True)
        case 'a' | 'amber':
            print('Check fuel line service routine.')
            troubleshoot(True)
        case 'r' | 'red':
            print('Shut-off al input lines check meter #3.')
            if prompt_digit('Meter (0-1000): ', METER_MIN, METER_MAX) < 50:
                print('Check main line for test pressure.')
                match prompt_text('Pressure (High/Normal/Low): ', PRESSURE_INPUTS):
                    case 'n' | 'normal':
                        print('Refer to motor service manual.')
                        troubleshoot(True)
                    case 'h' | 'high' | 'l' | 'low':
                        print('Refer to main line manual.')
                        troubleshoot(True)
                    case _:
                        goodbye()
            else:
                print('Measure flow velocity at inlet 2-B.')
                match prompt_text('Velocity (High/Normal/Low): ', PRESSURE_INPUTS):
                    case 'n' | 'normal':
                        print('Refer to inlet service manual.')
                        troubleshoot(True)
                    case 'h' | 'high' | 'l' | 'low':
                        print('Refer unit for factory service.')
                        troubleshoot(True)
                    case _:
                        goodbye()
        case _:
            goodbye()


# trigger recursive chain
troubleshoot()
