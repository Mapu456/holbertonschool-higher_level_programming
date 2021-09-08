#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    long = len(sys.argv)
    long = long - 1
    if long == 1:
        print("{:d} argument".format(long))
    elif long == 0 or long > 1:
        print("{:d} arguments".format(long))
    arg0 = sys.argv[1:]
    count = 0
    for arguments in arg0:
        count += 1
        print("{:d} : {:s}".format(count, arguments))
