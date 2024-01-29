"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""


def get_sales_tax(subtotal: float) -> float:
    """Returns the tax amount given subtotal value."""
    return subtotal * 0.07


def dollarize(amount: float) -> str:
    """Returns the currency string given a number."""
    return '$' + format(amount, ',.2f')


# pylint: disable=invalid-name, consider-using-enumerate
def multiplyMatrix(a: list, b: list) -> list:
    """Returns the multiplication of 2-D matrices.

    :param a: the first matrix.
    :param b: the second matrix.
    """
    if len(a[0]) != len(b):
        raise ValueError('Incompatible sizes.')
    c = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c
