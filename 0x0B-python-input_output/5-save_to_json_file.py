#!/usr/bin/python3
"""
to_json_string function
"""
import json


def save_to_json_file(my_obj, filename):
    '''
    returns the JSON representation of an object (string)
    '''
    with open('filename', 'w', encoding='utf-8') as f:
        return(json.dumps(my_obj))
