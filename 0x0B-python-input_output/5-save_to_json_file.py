#!/usr/bin/python3
"""save object to json file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    object to json saved into a file
        args:
            my_obj: object
            filename: json file
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
