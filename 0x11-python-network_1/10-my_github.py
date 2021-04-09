#!/usr/bin/python3
"""
python script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    jstring = r.json()
    print(jstring.get('id'))
