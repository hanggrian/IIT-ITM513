"""
Assignment #6
Convert LDAP data structure and validate phone numbers using regular expression.

Author: Hendra Wijaya (A20529195)
"""

from re import match, findall

INPUT_PHONES = 'phones_input.txt'
OUTPUT_PHONES = 'phones_output.txt'

REGEX = r'^(?:\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}|\d{10})$'

END = '\033[0m'
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'

print()
print(f"{BOLD}Reading '{INPUT_PHONES}'{END}")
print()

output_correct: str = ''
output_incorrect: str = ''
with open(INPUT_PHONES, 'r', encoding='UTF-8') as f:
    for line in f.read().splitlines()[1:]:
        if match(REGEX, line):
            digits: str = ''.join(findall(r'\d+', line))
            converted_line = f'({digits[:3]}) {digits[3:6]} {digits[6:]}'
            print(f'{GREEN}{line} → {converted_line}{END}')
            output_correct += converted_line + '\n'
        else:
            print(f'{RED}{line}{END}')
            output_incorrect += line + '\n'

print()
print(f"{BOLD}Writing '{OUTPUT_PHONES}'{END}")
print()

chunks = f'{output_correct}\n{output_incorrect}'.split('\n')
for i in range(0, 4):
    print(f'{chunks[i]}')
print('...')

with open(OUTPUT_PHONES, 'w', encoding='UTF-8') as f:
    f.write(f'Correct:\n{output_correct}\nIncorrect:\n{output_incorrect}')

print()
print('Goodbye!')
print()
