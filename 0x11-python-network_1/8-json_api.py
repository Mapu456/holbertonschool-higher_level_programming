#!/usr/bin/python3
"""take URL, send a POST request to the passed URL
    with the email, and displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        value = {'q': ""}
    else:
        value = {'q': argv[1]}
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', value)
        json = response.json()
        if json:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except:
        print("Not a valid JSON")
