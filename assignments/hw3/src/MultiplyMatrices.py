# pylint: disable=invalid-name
"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""

from calculator import multiplyMatrix


def prompt_matrix(message: str) -> list:
    """Recursively ask user for a 3x3 matrix.

    :param message: a space-separated decimals.
    :return: 2-D list.
    """
    s = input(message).strip()
    if not s:
        return prompt_matrix('Cannot be empty, try again... ')
    split = s.split(' ')
    if len(split) != 9:
        return prompt_matrix('Incorrect size, try again... ')
    try:
        return [[float(split[0]), float(split[1]), float(split[2])],
                [float(split[3]), float(split[4]), float(split[5])],
                [float(split[6]), float(split[7]), float(split[8])]]
    except ValueError:
        return prompt_matrix('Parsing error, try again... ')


def get_longest_element_length(matrix: list) -> int:
    """Determines the longest length of an element in this list."""
    length = 0
    for line in matrix:
        for e in line:
            length = max(length, len(f'{e:g}'))
    return length


def stringify_element(num: float, length: int):
    """Add extra whitespace padding for pretty printing."""
    s = f'{num:g}'
    spaces = ''
    for _ in range(length - len(s)):
        spaces += ' '
    return s + spaces


print()
print('3x3 matrix is a space-separated value of 9 decimals')

matrix1 = prompt_matrix('Enter matrix1: ')
matrix2 = prompt_matrix('Enter matrix2: ')
matrix3 = multiplyMatrix(matrix1, matrix2)
length1 = get_longest_element_length(matrix1)
length2 = get_longest_element_length(matrix2)
length3 = get_longest_element_length(matrix3)

print('The multiplication of the matrices is')
print(
    f'{stringify_element(matrix1[0][0], length1)} ' +
    f'{stringify_element(matrix1[0][1], length1)} ' +
    f'{stringify_element(matrix1[0][2], length1)}     ' +
    f'{stringify_element(matrix2[0][0], length2)} ' +
    f'{stringify_element(matrix2[0][1], length2)} ' +
    f'{stringify_element(matrix2[0][2], length2)}     ' +
    f'{stringify_element(matrix3[0][0], length3)} ' +
    f'{stringify_element(matrix3[0][1], length3)} ' +
    f'{stringify_element(matrix3[0][2], length3)}',
)
print(
    f'{stringify_element(matrix1[1][0], length1)} ' +
    f'{stringify_element(matrix1[1][1], length1)} ' +
    f'{stringify_element(matrix1[1][2], length1)}  ×  ' +
    f'{stringify_element(matrix2[1][0], length2)} ' +
    f'{stringify_element(matrix2[1][1], length2)} ' +
    f'{stringify_element(matrix2[1][2], length2)}  =  ' +
    f'{stringify_element(matrix3[1][0], length3)} ' +
    f'{stringify_element(matrix3[1][1], length3)} ' +
    f'{stringify_element(matrix3[1][2], length3)}',
)
print(
    f'{stringify_element(matrix1[2][0], length1)} ' +
    f'{stringify_element(matrix1[2][1], length1)} ' +
    f'{stringify_element(matrix1[2][2], length1)}     ' +
    f'{stringify_element(matrix2[2][0], length2)} ' +
    f'{stringify_element(matrix2[2][1], length2)} ' +
    f'{stringify_element(matrix2[2][2], length2)}     ' +
    f'{stringify_element(matrix3[2][0], length3)} ' +
    f'{stringify_element(matrix3[2][1], length3)} ' +
    f'{stringify_element(matrix3[2][2], length3)}',
)
print()
