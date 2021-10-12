#!/usr/bin/python3
"""Creates an object from a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Write JSON object to the file text
    Args:
        my_obj (object): python object
        filename (txt): JSON file text
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(json.dumps(my_obj)))
