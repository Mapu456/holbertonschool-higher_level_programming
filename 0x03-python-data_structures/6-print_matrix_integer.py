#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for initial in matrix:
        for i in initial:
            print("{:d}".format(i), end="")
            if i != initial[-1]:
                print(" ", end="")
        print()
