#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        return list(map(lambda i: i if i != search else replace, my_list))
