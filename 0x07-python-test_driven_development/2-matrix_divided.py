#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    function that divids matrix by a number

    Args:
        matrix (list): contains lists
        div (int/float): divisor
    Raises:
        TypeError: if matrix has no lists
        TypeError: If rows are not equal
        TypeError: if elements are not int/float
        ZeroDivisionError: if divisor 0
    Returns:
        Returns matrix of lists with the divided numbers
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix == []:
        raise TypeError(msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(msg)
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError(msg)
    if not isinstance(div, (float, int)):
        raise TypeError(msg)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(y / div, 2) for y in row] for row in matrix]
