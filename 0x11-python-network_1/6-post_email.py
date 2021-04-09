#!/usr/bin/python3
"""
python script sends a POST request to the passed
URL with the email as a parameter, and finally
displays the body of the response
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(url, data)
    print(r.text)
