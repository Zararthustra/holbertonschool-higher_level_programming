#!/usr/bin/python3
"""json to object module
"""
import json


def from_json_string(my_str):
    """
    load string
    	args:
	    my_str: string to load
    """
    return json.loads(my_str)
