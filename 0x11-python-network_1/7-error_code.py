#!/usr/bin/python3
'''script for Error code: takes in a URL, sends a request to the
   URL and displays the body of the response (decoded in utf-8)'''
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as l:
            print(l.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
