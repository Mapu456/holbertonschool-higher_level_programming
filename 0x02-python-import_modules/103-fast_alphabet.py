#!/usr/bin/python3
if __name__ == "__main__":
    str = ""

    def uppercase(str_data):
        return (str.join([chr(ord(char) - 32) for char in str_data if ord(char) >= 65]))

    print(uppercase("abcdefghijlmnopqrstuvwxyz"))
