#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for initial in matrix:
        for i in initial:
            return list(map(lambda initial: list(map(lambda i: i ** 2, initial)),
			matrix))
