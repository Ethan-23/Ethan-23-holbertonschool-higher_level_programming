#!/usr/bin/python3
"""Comment"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(argv[1], argv[2])).json()
    print(req.get('id'))
