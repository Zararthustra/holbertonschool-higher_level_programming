#!/usr/bin/python3
"""
geometry class and sublclass
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    empty class
    """
    def __init__(self, width, height):
        """
        constructor
            args:
                width: width
                height: height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
