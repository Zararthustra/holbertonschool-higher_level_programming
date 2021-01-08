#!/usr/bin/python3
"""
add_integer - add func with secure checks
"""


def add_integer(a, b=98):
    """
    sum of two ints
        args:
            a: int
            b: int
        return:
            sum if OK, raise error if failure
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
