#!/usr/bin/python3
def weight_average(my_list=[]):
	if not my_list:
		return 0
	return list(map(lambda initial: list(map(lambda i, c: ((i * c)/c), initial)),
	my_list))
