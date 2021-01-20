#!/usr/bin/python3
"""save to json file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    object string to json saved into a file
        args:
            my_obj: string
            filename: json file
    """
    obj = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(obj)
