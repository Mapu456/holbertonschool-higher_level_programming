#!/usr/bin/python3
for c in range(0, 10):
    for i in range(0, 10):
        if c == 8 and i == 9:
            print("{:d}{:d}".format(c, i), end="\n")
        elif c == 1 and i == 0:
            continue
        elif c < i:
            print("{:d}{:d}".format(c, i), end=", ")
