"""
Assignment #14
Study of big data and SQLite integration with some command executions.

Author: Hendra Wijaya (A20529195)
"""

from sqlite3 import connect

from prompts import prompt_text

END = '\033[0m'
UNDERLINE = '\033[4m'
GREEN = '\033[32m'
YELLOW = '\033[33m'

ALPHABETS = 'abcde'

alphabet_counter: int = 0

connection = connect('books.db')


def print_header(header):
    """Convenient method to print question headline."""
    global alphabet_counter  # pylint: disable=invalid-name, global-statement
    print()
    print(f'{ALPHABETS[alphabet_counter]}. {header}')
    alphabet_counter = alphabet_counter + 1


def execute_command(command):
    """Convenient display SQL command execution result."""
    cursor = connection.cursor()
    is_insert = True
    rows = cursor.execute(command)
    for row in rows:
        is_insert = False
        print(f'{GREEN}{row}{END}')
    if is_insert:
        print(f'{GREEN}Success{END}')
    cursor.close()
    return rows


print_header("Select all authors' last names from the authors table in descending order.")
author_last_names = execute_command('SELECT last FROM authors ORDER BY last DESC')

print_header('Select all book titles from the titles table in ascending order.')
execute_command('SELECT title FROM titles ORDER BY title ASC')

print_header(
    'Use an INNER JOIN to select all the books for a specific author. Include the title, ' +
    'copyright year and ISBN. Order the information alphabetically by title.',
)
author_last_name = prompt_text(
    f"{YELLOW}Author's last name to search (" +
    f'{UNDERLINE}Deitel{END}{YELLOW}/' +
    f'{UNDERLINE}Quirk{END}{YELLOW}/' +
    f'{UNDERLINE}Wald{END}{YELLOW}):{END}',
    ['deitel', 'quirk', 'wald'],
)
execute_command(
    f'''
    SELECT titles.title, titles.copyright, titles.isbn FROM titles
      INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
      INNER JOIN authors ON author_ISBN.id = authors.id
    WHERE LOWER(authors.last) = '{author_last_name}'
    ORDER BY titles.title ASC;
    ''',
)

print_header('Insert a new author into the authors table.')
execute_command("INSERT INTO authors (first, last) VALUES ('John', 'Doe');")

print_header(
    'Insert a new title for an author. Remember that the book must have an entry in the ' +
    'author_ISBN table and an entry in the titles table.',
)
execute_command("INSERT INTO author_ISBN (id, isbn) VALUES (6, '0123456789')")

connection.close()

print()
print('Goodbye!')
print()
