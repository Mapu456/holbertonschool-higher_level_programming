#!/usr/bin/python3
if __name__ == "__main__":
    str = ''
    print((str.join([chr(ord(char) - 32) for char in "abcdefghijlmnopqrstuvwxyz" if ord(char) >= 65])))
