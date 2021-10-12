#!/usr/bin/python3
"""Square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square class
    Rectangle (BaseGeometry): subclass of BaseGeometry
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Implement area method
        """
        return self.__size * self.__size
