#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary.items())
    for i, x in order:
        print("{:s}: {}".format(i, x))
