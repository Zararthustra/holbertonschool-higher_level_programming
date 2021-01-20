#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as myFile:
        char_num = myFile.write(text)
        return char_num
