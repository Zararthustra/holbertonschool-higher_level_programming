#!/usr/bin/python3
"""read_file module
"""


def read_file(filename=""):
    """
    opens and reads a file
        args:
            filename: file name
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
