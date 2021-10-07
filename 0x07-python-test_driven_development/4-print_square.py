#!/usr/bin/python3
"""Module that print a square of strings
"""


def print_square(size):
    """Function to print the name and last name
        size is the size length of the square
        size must be an integer, otherwise raise a TypeError
        if size is less than 0, raise a ValueError
        if size is a float and is less than 0, raise a TypeError
        Print a square of strings
    """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
