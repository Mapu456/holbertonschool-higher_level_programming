#!/usr/bin/python3
"""returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Args:
        n, number of colums of triangle pascal
    """
    init_pascal = 1
    i = 0
    c = 0
    triangle = []
    while i < n:
        pascal = []
        while c < i+1:
            if c == 0 or c >= len(triangle):
                pascal.append(init_pascal)
            else:
                new_pascal = triangle[i-1][c] + triangle[i-1][c-1]
                pascal.append(new_pascal)
            c += 1
        triangle.append(pascal)
        c = 0
        i += 1
    return triangle
