#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited
from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is instance or inheritance
        args:
            obj: object to check
            a_class: class to check
        return:
            True if yes, False if no
    """
    return isinstance(obj, a_class)
