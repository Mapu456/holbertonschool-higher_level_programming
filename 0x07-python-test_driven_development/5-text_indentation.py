#!/usr/bin/python3
"""function that add two integers"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == ' ' and text[i - 1] == '.' or text[i - 1] == '?' or text[i - 1] == ':':
            while text[i] == ' ':
                i += 1
            print("")
            print("")
        print("{}".format(text[i]), end="")
        i += 1
