#!/usr/bin/python3
"""Function that reads a text file
    and prints it in the stdout
"""


def read_file(filename=""):
    """Read and print a text file
    Args:
        filename: Text file. Defaults to "".
    """
    with open(filename, encoding='utf-8') as f:
        read = f.read()
        print(read, end="")
