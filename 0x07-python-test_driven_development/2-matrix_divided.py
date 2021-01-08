#!/usr/bin/python3
"""
matrix_divided - divide matrix nums
"""


def matrix_divided(matrix, div):
    """
    divide matrix nums
        args:
            matrix: [[mat][rix]]
            div: dividor
        return:
            division if OK, raise error if failure
    """
    len_m = len(matrix[0])
    pep8 = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) is not list:
            raise TypeError(pep8)
        if len(i) != len_m:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(pep8)

    return [[round(j / div, 2) for j in i] for i in matrix]
