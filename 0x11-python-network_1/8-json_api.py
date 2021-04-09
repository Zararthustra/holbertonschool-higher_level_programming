#!/usr/bin/python3
"""
python script takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    data = {}
    if len(sys.argv) >= 2:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        jstring = r.json()
        if jstring == {}:
            print("No result")
        else:
            print("[{}] {}".format(jstring['id'], jstring['name']))
    except Exception as err:
        print("Not a valid JSON")
