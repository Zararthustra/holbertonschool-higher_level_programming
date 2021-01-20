#!/usr/bin/python3
"""dict module
"""

def class_to_json(obj):
    """
    return the dictionary description with simple data structure
    	args:
	    obj: object
    """
    return obj.__dict__
