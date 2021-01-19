#!/usr/bin/python3
"""
geometry class and sublclass
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    empty class
    """
    def __init__(self, size):
        """
        constructor
            args:
                size: size
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
