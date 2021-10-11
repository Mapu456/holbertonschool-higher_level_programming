#!/usr/bin/python3
"""Module for 'is_same_class' method"""


def is_same_class(obj, a_class):
    """verify the type of obj
    Arguments:
        obj: object to check
        a_class: class to be checked
    Return:
        True or false
    """
    return (type(obj) is a_class)
