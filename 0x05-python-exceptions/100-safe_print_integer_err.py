#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as stderr:
        sys.stderr.write("Exception: {}".format(stderr))
        return (False)
    return (True)
