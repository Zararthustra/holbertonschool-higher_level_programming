#!/usr/bin/python3
"""
python script displays the value of the variable
X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
