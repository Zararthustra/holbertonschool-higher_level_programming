#!/usr/bin/python3
"""student class module
"""


class Student:
    """
    student class
    """

    def __init__(self, first_name, last_name, age):
        """
        constructor
            args:
                first_name: str
                last_name: str
                age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return dict
        """
        return self.__dict__
