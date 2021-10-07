#!/usr/bin/python3
"""Module that print a name
"""


def say_my_name(first_name, last_name=""):
    """Function to print the name and last name
        first_name and last_name must be strings otherwise, raise a TypeError
        Print a name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
