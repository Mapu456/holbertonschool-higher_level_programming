#!/usr/bin/python3
"""function for lookup"""

from models.base import Base

class Rectangle(Base):
    """Read and print a text file
        Args:
    filename: Text file. Defaults to "".
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, id):
        return self.__width

    @height.setter
    def height(self, id):
        return self.__height

    @x.setter
    def x(self, id):
        return self.__x

    @y.setter
    def y(self, id):
        return self.__y
