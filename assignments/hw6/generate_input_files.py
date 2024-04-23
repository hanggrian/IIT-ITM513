"""
Assignment #6
Convert LDAP data structure and validate phone numbers using regular expression.

Author: Hendra Wijaya (A20529195)
"""

import sys
from datetime import datetime, timezone, timedelta

from faker import Faker
from faker.providers.phone_number import Provider

INPUT_LDAP = 'ldap_input.txt'
INPUT_PHONES = 'phones_input.txt'
ENTRIES_LDAP = 4
ENTRIES_PHONES = 16


class LdapProvider(Provider):
    """Standard US phone number format."""
    formats = ('###-###-####',)


class PhonesProvider(Provider):
    """Multiple formats half of which are incorrect."""
    formats = (
        '###-###-####', '(###) #######', '(###) ### ####', '##########',  # acceptable
        '###-####-###', '(###) ###-####',  # invalid format
        '(###) ########', '#########',  # not 10 digits
    )


if __name__ != '__main__':
    sys.exit(0)

ldap_faker = Faker(locale='en_US')
ldap_faker.add_provider(LdapProvider)

phones_faker = Faker(locale='en_US')
phones_faker.add_provider(PhonesProvider)

formatted_time = datetime.now(timezone(timedelta(hours=7))).strftime('%b %d %I:%M%p')

ldap_text = f'# Generated at {formatted_time}\n'
for _ in range(ENTRIES_LDAP):
    first_name = ldap_faker.first_name()
    last_name = ldap_faker.last_name()
    ldap_text += f'{first_name[0].lower()}{last_name.lower()}:'
    ldap_text += f'{first_name}:{last_name}:'
    ldap_text += f'{ldap_faker.phone_number()}\n'  # Linux recommends final newline

phones_text = f'# Generated at {formatted_time}\n'
for _ in range(ENTRIES_PHONES):
    phones_text += f'{phones_faker.phone_number()}\n'

print()
print(f'Writing {INPUT_LDAP}.')

with open(INPUT_LDAP, 'w', encoding='UTF-8') as file:
    file.write(ldap_text)

print(f'Writing {INPUT_PHONES}.')

with open(INPUT_PHONES, 'w', encoding='UTF-8') as file:
    file.write(phones_text)

print()
print('Goodbye!')
print()
