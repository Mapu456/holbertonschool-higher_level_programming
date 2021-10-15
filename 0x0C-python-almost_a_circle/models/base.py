#!/usr/bin/python3
"""function for lookup"""


class Base():
    """Read and print a text file
Args:
    filename: Text file. Defaults to "".
"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
