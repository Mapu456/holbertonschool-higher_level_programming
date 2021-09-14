#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda initial: list(map(lambda i: i ** number, initial)),
                    my_list))
