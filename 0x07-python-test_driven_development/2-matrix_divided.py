#!/usr/bin/python3
"""function that add two integers"""


def matrix_divided(matrix, div):
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for num in i:
            if type(num) is not int and type(num) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
