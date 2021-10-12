#!/usr/bin/python3
"""Creates an object from a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Creates an object from a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
