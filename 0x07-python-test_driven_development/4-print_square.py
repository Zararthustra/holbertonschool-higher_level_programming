#!/usr/bin/python3
"""
print_square - Prints a square with #
"""


def print_square(size):
    """
    prints a square filled with #
        args:
            size: size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) is float:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print("")
