#!/usr/bin/python3
"""take URL, send a POST request to the passed URL
    with the email, and displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    value = {'email': argv[2]}
    response = requests.post(argv[2], value)
    print(response.text)
