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
        Return: Square area
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

    def my_print(self):
        """
        Print square method
        """
        size = self.__size
        if size == 0:
            print("")
        else:
            for i in range(size):
                for j in range(size):
                    print('#', end="")
                print("")
