#!/usr/bin/python3
"""
function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    checks if obj is instance of subclass
        args:
            obj: object to check
            a_class: class to check
        return:
            True if yes, False if no
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
