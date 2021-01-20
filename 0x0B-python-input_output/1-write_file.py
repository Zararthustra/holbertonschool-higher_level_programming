#!/usr/bin/python3
"""write_file module
"""


def write_file(filename="", text=""):
    """
    opens and writes into a file
    	args:
	    filename: file name
	    text: text to write
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        char_num = myFile.write(text)
        return char_num
