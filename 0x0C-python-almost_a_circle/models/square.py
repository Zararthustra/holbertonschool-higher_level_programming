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
        """
        self.width = value
        self.height = value
