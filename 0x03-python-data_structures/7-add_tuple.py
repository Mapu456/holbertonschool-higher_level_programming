#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	lon = len(tuple_a)
	lon1 = len(tuple_b)
	if lon < 2 or lon1 < 2:
		print("0, 0")
	return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
