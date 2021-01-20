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

    def to_json(self, attrs=None):
        """
        retrieves a dict rpzation of a Student instance
            args:
                attrs: attributes
            return:
                dict
        """
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    D = {k: v for k, v in self.__dict__.items() if k in attrs}
                    return D
        return self.__dict__

    def reload_from_json(self, json):
        """
        replace keys and values
            args:
                json: dict
        """
        for key, value in json.items():
            setattr(self, key, value)
