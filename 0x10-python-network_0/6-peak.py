#!/usr/bin/python3
def findnum(list_of_integers):
    n = len(list_of_integers)
    num = list_of_integers[0]
    for i in range(1, n):
        if list_of_integers[i] >= num:
            num = list_of_integers[i]
        elif list_of_integers[i] >= 0:
            break
    return num
 
 
def find_num(list_of_integers):
    if list_of_integers == []:
        return "None"
    return findnum(list_of_integers)
