#!/usr/bin/python3
"""function for lookup"""

import json


class Base():
    """function for lookup"""

    __nb_objects = 0

    def __init__(self, id=None):
        """function for lookup"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function for lookup"""
        if list_dictionaries is None or not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function for lookup"""
        list = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write(list)
            else:
                for i in range(len(list_objs)):
                    list.append(cls.to_dictionary(list_objs[i]))
                file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """function for lookup"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function for lookup"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """function for lookup"""
        new_dict = []
        if ("{}.json".format(cls.__name__)) is not None:
            with open("{}.json".format(cls.__name__), 'r') as file_read:
                list_dict = cls.from_json_string(file_read.read())
                for i in list_dict:
                    new_dict.append(cls.create(**i))
        return (new_dict)
