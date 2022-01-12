#!/usr/bin/python3
def findPeak(list_of_integers, left=None, right=None):
    n = len(list_of_integers)
    if left is None and right is None:
        left, right = 0, len(list_of_integers) - 1
    mid = (left + right) // 2
    if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (mid == n - 1 or list_of_integers[mid + 1] <= list_of_integers[mid])):
        return mid
    if mid - 1 >= 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return findPeak(list_of_integers, left, mid - 1)
    return findPeak(list_of_integers, mid + 1, right)
 
 
def find_peak(list_of_integers):
    if list_of_integers == []:
        return "None"
    index = findPeak(list_of_integers)
    return list_of_integers[index]
