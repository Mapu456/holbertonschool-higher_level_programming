#!/usr/bin/python3
for c in range(0, 100):
    if c == 99:
        print("{:d}".format(c), end=" ")
    elif c < 10:
        print("0{:d}, ".format(c), end=" ")
    else:
        print("{:d}, ".format(c), end=" ")
print(" ")
