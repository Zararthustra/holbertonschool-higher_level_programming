#!/usr/bin/python3
"""
implementing magic methods eq and ne
"""


class MyInt(int):
    """
    MyInt class
    """

    def __eq__(self, other):
        """
        equal to method
        """
        return int(self) != other

    def __ne__(self, other):
        """
        not equal to method
        """
        return int(self) == other
