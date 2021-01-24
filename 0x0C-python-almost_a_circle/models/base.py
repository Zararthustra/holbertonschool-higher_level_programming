#!/usr/bin/python3
"""
base class module
"""


class Base:
    """
    init class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
            args:
                id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects