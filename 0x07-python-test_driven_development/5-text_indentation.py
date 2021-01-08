#!/usr/bin/python3
"""
text_indentation - Prints string indented
"""


def text_indentation(text):
    """
    print \n\n when ".?:" in text
        args:
            text: str to indent
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    cpy = ""
    x = 0
    for i in text:
        cpy += text[x]
        if text[x] in ".?:":
            print(cpy.strip())
            print()
            cpy = ""
        x += 1
    print(cpy.strip(), end="")
