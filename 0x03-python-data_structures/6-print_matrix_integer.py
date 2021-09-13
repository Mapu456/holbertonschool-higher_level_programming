#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	for initial in matrix:
	    lon = len(initial)
	    for i in initial:
	        print(i, end = " ")
	    print(" ")
