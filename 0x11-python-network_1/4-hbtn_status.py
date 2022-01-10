#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    request_g = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    txt = request_g.text
    print("\t- type:", type(txt))
    print("\t- content:", txt)
