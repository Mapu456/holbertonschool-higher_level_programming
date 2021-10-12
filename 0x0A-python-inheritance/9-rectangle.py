#!/usr/bin/python3
"""Module BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Empty class BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """this Method print area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """this Method return Rectangle"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
