#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    obj = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(obj)