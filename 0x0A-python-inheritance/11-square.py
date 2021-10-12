#!/usr/bin/python3
"""Module BaseGeometry class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """this Method print area of rectangle"""
        return (Rectangle.area(self))

    def __str__(self):
        """this Method return Rectangle"""
        return ("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))