#!/usr/bin/python3
"""Module for read the file with read_file method"""


def write_file(filename="", text=""):
    with open('filename', 'w', encoding='utf-8') as f:
        read_data = f.write(text)
        return(read_data)
