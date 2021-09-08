#!/usr/bin/python3
def uppercase(str_data):
    return ''.join([chr(ord(char) - 32) for char in str_data if ord(char) >= 65])


print(uppercase())
