#!/usr/bin/python3
import os


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")