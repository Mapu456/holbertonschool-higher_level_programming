#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        number = ord(letter)
        if 96 < number < 123:
            number = number - 32
        print("{:c}".format(number), end="")
    print("")
