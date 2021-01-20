#!/usr/bin/python3
"""load from json file module
"""
import json


def load_from_json_file(filename):
    """
    open and load json file
        args:
            filename: json file to load
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        to_load = myFile.read()
        return json.loads(to_load)
