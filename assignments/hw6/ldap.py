"""
Assignment #6
Convert LDAP data structure and validate phone numbers using regular expression.

Author: Hendra Wijaya (A20529195)
"""

import sys

from generate_input_files import INPUT_LDAP

OUTPUT_LDAP = 'ldap_output.txt'

END = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[32m'

if __name__ != '__main__':
    sys.exit(0)

print()
print(f"{BOLD}Reading '{INPUT_LDAP}'{END}")
print()
print('dc=com')
print('└─ dc=example')

output: str = ''
with open(INPUT_LDAP, 'r', encoding='UTF-8') as file:
    lines = file.read().splitlines()[1:]
    for i, line in enumerate(lines):
        is_last = i == len(lines) - 1
        split = line.split(':')
        username = split[0]
        first_name = split[1]
        last_name = split[2]
        phone = split[3]

        if not is_last:
            print(f'   ├─ uid={GREEN}{username}{END}')
            print(f'   │  ├─ cn={GREEN}{first_name} {last_name}{END}')
            print(f'   │  ├─ sn={GREEN}{last_name}{END}')
            print(f'   │  └─ telephoneNumber={GREEN}{phone}{END}')
        else:
            print(f'   └─ uid={GREEN}{username}{END}')
            print(f'      ├─ cn={GREEN}{first_name} {last_name}{END}')
            print(f'      ├─ sn={GREEN}{last_name}{END}')
            print(f'      └─ telephoneNumber={GREEN}{phone}{END}')

        output += f'dn: uid={username}, dc=example, dc=com\n'
        output += f'cn: {first_name} {last_name}\n'
        output += f'sn: {last_name}\n'
        output += f'telephoneNumber: {phone}\n'
        if not is_last:
            output += '\n'

print()
print(f"{BOLD}Writing '{OUTPUT_LDAP}'{END}")
print()

spacing: str = '\n\n'
print(f"{output.split(f'{spacing}')[0]}")
print('...')

with open(OUTPUT_LDAP, 'w', encoding='UTF-8') as file:
    file.write(output)

print()
print('Goodbye!')
print()
