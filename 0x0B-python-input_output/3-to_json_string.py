#!/usr/bin/python3
"""object to json module
"""
import json


def to_json_string(my_obj):
    """
    dump string
        args:
            my_obj: object to dump
    """
    return json.dumps(my_obj)
