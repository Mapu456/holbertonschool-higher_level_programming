#!/usr/bin/python3
"""function for lookup"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        new_dict = dict()
        for key, value in list_objs.items:
            return
        with open("{}.json".format(cls.__name__), "w") as file:
            return file.write()