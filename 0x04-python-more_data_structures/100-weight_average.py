#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mult = 0
    sum2 = 0
    for i in my_list:
        sum2 += i[1]
        mult += i[0] * i[1]
        total = mult/sum2
    return total
