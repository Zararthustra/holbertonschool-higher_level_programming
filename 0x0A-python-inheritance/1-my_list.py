#!/usr/bin/python3
"""
geometry class and sublclass
"""


class MyList(list):
    """
    class that inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
