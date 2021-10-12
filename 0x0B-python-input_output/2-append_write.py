#!/usr/bin/python3
"""Module for read the file with read_file method"""


def append_write(filename="", text=""):
    """Read and print a text file
    Args:
        filename: Text file.""
    """
    with open(filename, 'a', encoding='utf-8') as f:
        read_data = f.write(text)
        return(read_data)
