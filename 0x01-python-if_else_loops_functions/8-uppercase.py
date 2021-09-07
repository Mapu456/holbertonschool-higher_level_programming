#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if letter == " ":
            letter = '~'
        if letter == '9':
            letter = '{'
        if letter == '8':
            letter = '}'
        number = ord(letter)
        if number < 96:
            number = number + 32
        if 96 < number < 127:
            number = number - 32
            if number == 94:
                number = 32
            if number == 91:
                number = 57
            if number == 93:
                number = 56
        print("{:c}".format(number), end="")
    print()
