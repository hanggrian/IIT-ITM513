"""
Assignment #3
List/array operations to calculate grand total with a sales tax and 2-D matrix multiplication.

Author: Hendra Wijaya (A20529195)
"""


def get_sales_tax(subtotal: float) -> float:
    """Returns the tax amount given subtotal value."""
    return subtotal * 0.07


def dollarize(value: float) -> str:
    """Returns the currency string given a number."""
    return f'${value:,.2f}'


def multiplyMatrix(a: list, b: list) -> list:  # pylint: disable=invalid-name
    """Returns the multiplication of 2-D matrices.

    :param a: the first matrix.
    :param b: the second matrix.
    """
    if len(a[0]) != len(b):
        raise ValueError('Incompatible sizes.')
    result: list[list[int]] = [[0] * len(b[0]) for _ in range(len(a))]
    # pylint: disable=consider-using-enumerate
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
