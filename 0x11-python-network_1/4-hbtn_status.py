#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    request_g = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('    - type: {}'.format(type(request_g.text)))
    print('    - content: {}'.format(request_g.text))
