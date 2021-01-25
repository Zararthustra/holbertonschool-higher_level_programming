#!/usr/bin/python3
"""
square class module
"""
from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor
            args:
                size (int): size
                x (int): indentation
                y (int): offset
                id (int): id
        """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """
        returns the dictionary representation of [Square]
        """
        dic = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return dic

    def update(self, *args, **kwargs):
        """
        assigns attributes
        """
        attributes = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key in kwargs.keys():
                if key in attributes:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """
        str magic method
        """
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        return "[Square] ({}) {}/{} - {}".format(a, b, c, d)

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
            args:
                value: value to set
        """
        self.width = value
        self.height = value
