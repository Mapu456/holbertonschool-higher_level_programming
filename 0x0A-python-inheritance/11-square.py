#!/usr/bin/python3
"""Module BaseGeometry class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """this Method return Rectangle"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))