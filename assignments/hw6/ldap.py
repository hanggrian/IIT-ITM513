"""
Assignment #6
Convert LDAP data structure and validate phone numbers using regular expression.

Author: Hendra Wijaya (A20529195)
"""

INPUT_LDAP = 'ldap_input.txt'
OUTPUT_LDAP = 'ldap_output.txt'

print()
print(f"Reading '{INPUT_LDAP}'...")
print()
print('dc=com')
print('└─ dc=example')

output: str = ''
with open('ldap_input.txt', 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()[1:]
    for i, line in enumerate(lines):
        is_last = i == len(lines) - 1
        split = line.split(':')
        username = split[0]
        first_name = split[1]
        last_name = split[2]
        phone = split[3]

        if not is_last:
            print(f'   ├─ uid={username}')
            print(f'   │  ├─ cn={first_name} {last_name}')
            print(f'   │  ├─ sn={last_name}')
            print(f'   │  └─ telephoneNumber={phone}')
        else:
            print(f'   └─ uid={username}')
            print(f'      ├─ cn={first_name} {last_name}')
            print(f'      ├─ sn={last_name}')
            print(f'      └─ telephoneNumber={phone}')

        output += f'dn: uid={username}, dc=example, dc=com\n'
        output += f'cn: {first_name} {last_name}\n'
        output += f'sn: {last_name}\n'
        output += f'telephoneNumber: {phone}\n'
        if not is_last:
            output += '\n'

print()
print(f"Writing '{OUTPUT_LDAP}'...")

with open(OUTPUT_LDAP, 'w', encoding='UTF-8') as f:
    f.write(output)

print('Done!')
print()
