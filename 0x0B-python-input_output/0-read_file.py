#!/usr/bin/python3
"""Module for read the file with read_file method"""


def read_file(filename=""):
    """Module for read the file with read_file method"""
    with open('filename', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end="")
