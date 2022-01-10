#!/usr/bin/python3
"""take URL, send a POST request to the passed URL
    with the email, and displays the body of the response
"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    value = {'email': argv[2]}
    data = parse.urlencode(value).encode("utf-8")
    with request.urlopen(argv[1], data) as response:
        print(response.read().decode("utf-8"))
