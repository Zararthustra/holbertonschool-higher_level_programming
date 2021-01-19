#!/usr/bin/python3
"""
function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    checks if obj is instance of a_class
        args:
            obj: object to check
            a_class: specified class
        return:
            True if yes, False if no
    """
    return type(obj) is a_class
