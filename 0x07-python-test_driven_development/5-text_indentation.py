#!/usr/bin/python3
"""Module that print a text with lines break
"""


def text_indentation(text):
    """Function to print the name and last name
        text must be a string, otherwise raise a TypeError
        There should be no space at the beginning or at the
        end of each printed line.
        Print a text with lines break
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i = i + 1
    while i < len(text):
        print("{:s}".format(text[i]), end="")
        if text[i] == "\n" or text[i] == '?'\
                or text[i] == ':' or text[i] == '.':
            if text[i] == '?' or text[i] == ':' or text[i] == '.':
                print("\n")
            i = i + 1
            while i < len(text) and text[i] == ' ':
                i = i + 1
            continue
        i = i + 1
