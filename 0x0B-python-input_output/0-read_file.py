#!/usr/bin/python3
"""Module for read the file with read_file method"""


def read_file(filename=""):
    """Read and print a text file
    Args:
        filename (str, optional): Text file. Defaults to "".
    """
    with open('filename', encoding='utf-8') as f:
        print(f.read(), end="")
