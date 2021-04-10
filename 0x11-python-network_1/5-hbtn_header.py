#!/usr/bin/python3
"""Comment"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
