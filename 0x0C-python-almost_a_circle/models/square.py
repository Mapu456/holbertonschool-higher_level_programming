#!/usr/bin/python3
"""function for lookup"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, number):
        self.width = number
        self.height = number

    def update(self, *args, **kwargs):
        return args

    def to_dictionary(self):
        return self.__dict__