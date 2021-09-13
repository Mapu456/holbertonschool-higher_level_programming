#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or (idx + 1) > length:
        return (None)
    else:
        for i in my_list:
            value = my_list[idx]
        return value
