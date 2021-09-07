#!/usr/bin/python3
def print_last_digit(number):
	if number < 0:
		number = number * -1
	for last_digit in str(number):
		last3 = int(last_digit[-1])
	print("{:d}".format(last3), end = "")
	return(last3)

