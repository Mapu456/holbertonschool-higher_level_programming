#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last2 = str(number)
last3 = int(last2[-1])
if number < 0:
    last3 = last3 * -1
if last3 == 0:
    print("Last digit of {:d} is {:d} and is 0".format(
        number, last3), end="\n")
elif last3 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(
        number, last3), end="\n")
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(
        number, last3), end="\n")
