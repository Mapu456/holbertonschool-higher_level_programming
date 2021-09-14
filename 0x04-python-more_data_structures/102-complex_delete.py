#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = {}
    new_dictionary = a_dictionary.copy()
    for value, values in new_dictionary.items():
        new_dictionary[value] = values * 2
    return new_dictionary
