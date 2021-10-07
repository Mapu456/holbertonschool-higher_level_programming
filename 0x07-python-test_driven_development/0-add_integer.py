#!/usr/bin/python3
"""Module to find the add_integer in a list
"""


def add_integer(a, b=98):
    """Function to return the sum between two integers
        a and b must be integers or floats, otherwise raise a TypeError
        Returns an integer: the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return(int(a + b))
