#!/usr/bin/python3
"""Module to know is instance of object or class"""


def is_kind_of_class(obj, a_class):
    """Function that checks of kind object. The isinstance()
    returns True if an object or variable is of a specified
    type otherwise False
    Arguments:
        obj: object to be checked
        a_class: class to be checked
    Return: True or false
    """
    return (isinstance(obj, a_class))
