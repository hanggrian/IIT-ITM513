"""
Assignment #14
Study of big data and SQLite integration with some command executions.

Author: Hendra Wijaya (A20529195)
"""

from sqlite3 import connect

END = '\033[0m'
BOLD = '\033[1m'

print()
print('Executing SQL command...')
print()

connection = connect('books.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM titles')

columns = [d[0] for d in cursor.description]
rows = cursor.fetchall()

# find the longest string of each cell
max_lengths = [len(column) for column in columns]
for row in rows:
    for i, cell in enumerate(row):
        max_lengths[i] = max(max_lengths[i], len(str(cell)))

# table pretty printing, separate with 2 spaces
print(
    f'{BOLD}{columns[0]:<{max_lengths[0]}}{END}  ' +
    f'{BOLD}{columns[1]:<{max_lengths[1]}}{END}  ' +
    f'{BOLD}{columns[2]:<{max_lengths[2]}}{END}  ' +
    f'{BOLD}{columns[3]:<{max_lengths[3]}}{END}',
)
for row in rows:
    print(
        f'{row[0]:<{max_lengths[0]}}  ' +
        f'{row[1]:<{max_lengths[1]}}  ' +
        f'{row[2]:<{max_lengths[2]}}  ' +
        f'{row[3]:<{max_lengths[3]}}',
    )

cursor.close()
connection.close()

print()
print('Goodbye!')
print()
