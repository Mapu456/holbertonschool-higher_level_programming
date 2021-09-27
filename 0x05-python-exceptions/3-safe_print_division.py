#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
        print("Inside result: {:d}".format(result))
    except ZeroDivisionError:
        result = None
    finally:
        return (result)
