#!/usr/bin/python3
"""
python script If the HTTP status code is greater than
or equal to 400, print: Error code: followed by the
value of the HTTP status code
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(r.text)
