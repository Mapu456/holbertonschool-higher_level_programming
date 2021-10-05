#!/usr/bin/python3
"""function that add two integers"""


def print_square(size):
	if type(size) is not int and type(size) is not float:
		raise TypeError("size must be an integer")
	if size < 0:
		raise ValueError("size must be >= 0")
	for i in range(size):
		print('#' * size)