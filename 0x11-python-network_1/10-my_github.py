#!/usr/bin/python3
"""take URL, send a POST request to the passed URL
    with the email, and displays the body of the response
"""
import requests
from sys import argv

from requests.api import request

if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(argv[1])
    request = requests.get(url, (argv[1], argv[2]))
    print(request.json().get("id"))
