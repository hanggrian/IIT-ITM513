# pylint: disable=invalid-name
"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""

END = '\033[0m'
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'


def multiplyMatrix(a, b):
    """Returns the multiplication of 2-D matrices.

    :param a: the first matrix.
    :param b: the second matrix.
    """
    if len(a[0]) != len(b):
        raise ValueError('Incompatible sizes.')
    result = [[0] * len(b[0]) for _ in range(len(a))]
    # pylint: disable=consider-using-enumerate
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def prompt_matrix(message):
    """Recursively ask user for a 3x3 matrix.

    :param message: a space-separated decimals.
    :return: 2-D list.
    """
    result = input(f'{message} ').strip()
    if not result:
        return prompt_matrix(f'{RED}Cannot be empty, try again...{END}')
    result = result.split(' ')
    if len(result) != 9:
        return prompt_matrix(f'{RED}Incorrect size, try again...{END}')
    try:
        return [
            [float(result[0]), float(result[1]), float(result[2])],
            [float(result[3]), float(result[4]), float(result[5])],
            [float(result[6]), float(result[7]), float(result[8])],
        ]
    except ValueError:
        return prompt_matrix(f'{RED}Parsing error, try again...{END}')


def get_longest_element_length(matrix):
    """Returns the longest length of an element in this list."""
    length = 0
    for line in matrix:
        for e in line:
            length = max(length, len(f'{e:g}'))
    return length


def stringify_element(num, length):
    """Add extra whitespace padding for pretty printing."""
    s = f'{num:g}'
    spaces = ''
    for _ in range(length - len(s)):
        spaces += ' '
    return s + spaces


def main():
    """The main function."""
    print()
    print(f'{BOLD}3x3 matrix is a space-separated value of 9 decimals{END}')
    print()

    matrix1 = prompt_matrix(f'{YELLOW}Enter matrix1:{END}')
    matrix2 = prompt_matrix(f'{YELLOW}Enter matrix2:{END}')
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
        f'{GREEN}{stringify_element(matrix3[0][0], length3)} ' +
        f'{stringify_element(matrix3[0][1], length3)} ' +
        f'{stringify_element(matrix3[0][2], length3)}{END}',
    )
    print(
        f'{stringify_element(matrix1[1][0], length1)} ' +
        f'{stringify_element(matrix1[1][1], length1)} ' +
        f'{stringify_element(matrix1[1][2], length1)}  ×  ' +
        f'{stringify_element(matrix2[1][0], length2)} ' +
        f'{stringify_element(matrix2[1][1], length2)} ' +
        f'{stringify_element(matrix2[1][2], length2)}  =  ' +
        f'{GREEN}{stringify_element(matrix3[1][0], length3)} ' +
        f'{stringify_element(matrix3[1][1], length3)} ' +
        f'{stringify_element(matrix3[1][2], length3)}{END}',
    )
    print(
        f'{stringify_element(matrix1[2][0], length1)} ' +
        f'{stringify_element(matrix1[2][1], length1)} ' +
        f'{stringify_element(matrix1[2][2], length1)}     ' +
        f'{stringify_element(matrix2[2][0], length2)} ' +
        f'{stringify_element(matrix2[2][1], length2)} ' +
        f'{stringify_element(matrix2[2][2], length2)}     ' +
        f'{GREEN}{stringify_element(matrix3[2][0], length3)} ' +
        f'{stringify_element(matrix3[2][1], length3)} ' +
        f'{stringify_element(matrix3[2][2], length3)}{END}',
    )

    print()
    print('Goodbye!')
    print()


if __name__ == '__main__':
    main()
