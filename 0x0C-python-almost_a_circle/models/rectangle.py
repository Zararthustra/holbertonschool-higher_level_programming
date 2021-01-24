#!/usr/bin/python3
"""
rectangle class module
"""
from models import base
Base = base.Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor
            args:
                width (int): width
                height (int): height
                x (int): x indentation
                y (int): y indentation
                id (int): id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        if kwargs:
            for key in kwargs.keys():
                if key in attributes:
                    setattr(self, key, kwargs[key])

    def display(self):
        """
        prints in stdout the Rectangle with '#'
        x, y for offset
        """
        for newline in range(self.y):
            print()
        for row in range(self.height):
            for space in range(self.x):
                print(' ', end="")
            for col in range(self.width):
                print('#', end="")
            print()

    def area(self):
        """
        return area
        """
        return self.width * self.height

    def __str__(self):
        """
        str magic method
        """
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        e = self.height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e)

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
