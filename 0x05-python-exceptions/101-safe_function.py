#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as stderr:
        sys.stderr.write("Exception: {}\n".format(stderr))
        res = None
    return (res)
