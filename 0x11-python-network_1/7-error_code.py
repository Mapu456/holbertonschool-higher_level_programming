#!/usr/bin/python3
'''script for Error code: takes in a URL, sends a request to the
   URL and displays the body of the response (decoded in utf-8)'''
import requests
from sys import argv


if __name__ == "__main__":
    request = requests.get(argv[1])
    print(request.text)
    if request.status_code >= 400:
        print('Error code: {}'.format(request.code))
    else:
        print('Index')
