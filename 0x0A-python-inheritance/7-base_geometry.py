#!/usr/bin/python3
"""
geometry class and sublclass
"""


class BaseGeometry:
    """
    empty class
    """
    def area(self):
        """
        area function
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        checks value
            args:
                name: string
                value: int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
