#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    long = len(sys.argv)
    long = long - 1
    if long == 1:
        print("{:d} argument".format(long - 1))
    elif long == 0 or long > 1:
        print("{:d} arguments".format(long - 1))
    arg0 = sys.argv[2:]
    count = 0
    for arguments in arg0:
        count += 1
        print("{:d} : {:s}".format(count, arguments))
