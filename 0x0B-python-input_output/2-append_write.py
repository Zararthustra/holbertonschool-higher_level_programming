#!/usr/bin/python3
"""append_write module
"""


def append_write(filename="", text=""):
    """
    append a text into a file
    	args:
	    filename: file to append text
	    text: text to append
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        char_num = myFile.write(text)
        return char_num
