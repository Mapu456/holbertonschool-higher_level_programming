#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value < 0:
            print("{:d}".format(value))
            return True
        elif value >= 0:
            print("{:d}".format(value))
            return True
        import sys
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
