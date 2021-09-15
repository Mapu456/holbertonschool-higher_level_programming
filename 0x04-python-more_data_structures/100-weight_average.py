#!/usr/bin/python3
def weight_average(my_list=[]):
	return list(map(lambda initial: list(map(lambda i, c: ((i * c)/c), initial)),
	my_list))
