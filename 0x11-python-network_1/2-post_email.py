#!/usr/bin/python3
"""
python script sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
"""


if __name__ == "__main__":
        from urllib import request, parse
        import sys

        email = {'email': sys.argv[2]}
        encoding = parse.urlencode(email)
        encoded = encoding.encode("utf-8")
        url = request.Request(sys.argv[1], encoded)

        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
