#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list[len(my_list):0:-1]
    for i in reversed_list:
        print("{:d}".format(i))
