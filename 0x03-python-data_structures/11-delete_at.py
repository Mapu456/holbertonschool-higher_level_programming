#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lon = len(my_list)
    if idx < 0 or (idx + 1) > lon:
        return my_list
    my_list.remove(idx + 1)
    return my_list
