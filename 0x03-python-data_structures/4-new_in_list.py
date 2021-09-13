#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or (idx + 1) > length:
        return(my_list)
    new_list = []
    for i in my_list:
        new_list.append(i)
    new_list[idx] = element
    return new_list
