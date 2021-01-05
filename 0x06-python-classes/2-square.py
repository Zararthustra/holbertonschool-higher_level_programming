#!/usr/bin/python3
"""
Class project - square class
"""


class Square:
    """
    Square Class
    """
    def __init__(self, size=0):
        """
        initialize square
            Args:
                size (int): Square size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
