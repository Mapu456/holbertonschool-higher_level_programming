#!/usr/bin/python3
"""
to_json_string function
"""
import json


def save_to_json_file(my_obj, filename):
    """Output JSON object as a string
    Args:
        my_obj: python object
    Returns:
        object: JSON object as a string
    """
    with open('filename', 'w', encoding='utf-8') as f:
        return (f.write(json.dumps(my_obj)))
