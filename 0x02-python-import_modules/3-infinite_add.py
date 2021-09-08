#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg0 = sys.argv[1:]
    sum = 0
    for arguments in arg0:
        sum += int(arguments)
    print("{:d}".format(sum))
