#!/usr/bin/python3
"""
Class project - square class
"""


class Square:
    """
    Square Class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize square
            Args:
                size (int): Square size
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Position getter
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Position setter
        """
        if type(value) is tuple and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) and isinstance(value[1], int):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Print square method
        """
        size = self.__size
        position = self.__position
        if size == 0:
            print("")
        else:
            for n in range(position[1]):
                print("")
            for i in range(size):
                for j in range(position[0]):
                    print(' ', end="")
                for k in range(size):
                    print('#', end="")
                print("")
