#!/usr/bin/python3
print(print((str.join([chr(ord(char) - 32)
      for char in "abcdefghijlmnopqrstuvwxyz" if ord(char) >= 65]))))
