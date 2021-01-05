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
        self.size = size

    def area(self):
        """
        Return: square area
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Size getter
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Size setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
