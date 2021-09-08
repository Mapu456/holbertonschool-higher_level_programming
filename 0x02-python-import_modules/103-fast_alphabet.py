#!/usr/bin/python3
def uppercase(str_data):
    print((''.join([chr(ord(char) - 32) for char in str_data if ord(char) >= 65])))
