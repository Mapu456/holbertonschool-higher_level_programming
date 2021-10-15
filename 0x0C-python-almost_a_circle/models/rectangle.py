#!/usr/bin/python3
"""function for lookup"""

from models.base import Base


class Rectangle(Base):
    """Read and print a text file
        Args:
    filename: Text file. Defaults to "".
        """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')
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
    def width(self, number):
        if type(number) is not int:
            raise TypeError("width must be an integer")
        if number <= 0:
            raise ValueError("width must be > 0")
        return self.__width

    @height.setter
    def height(self, number):
        if type(number) is not int:
            raise TypeError("height must be an integer")
        if number <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, number):
        if type(number) is not int:
            raise TypeError("x must be an integer")
        if number < 0:
            raise ValueError("x must be >= 0")
        return self.__x

    @y.setter
    def y(self, number):
        if type(number) is not int:
            raise TypeError("y must be an integer")
        if number < 0:
            raise ValueError("y must be >= 0")
        return self.__y

    def area(self):
        return self.__height * self.__width

    def display(self):
        for c in range(self.__y):
            print('')
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args):
        return args
