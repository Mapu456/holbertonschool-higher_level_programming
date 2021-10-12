#!/usr/bin/python3
"""Module BaseGeometry class"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Empty class BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation  private attributes and validate are ints"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
