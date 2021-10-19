#!/usr/bin/python3
"""function for lookup"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """function for lookup"""
    def __init__(self, size, x=0, y=0, id=None):
        """function for lookup"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """function for lookup"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """function for lookup"""
        return self.width

    @size.setter
    def size(self, number):
        """function for lookup"""
        self.width = number
        self.height = number

    def update(self, *args, **kwargs):
        """function for lookup"""
        key = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, key[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """function for lookup"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
