#!/usr/bin/python3
"""THIS IS A COMMENT"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    emaildict = {'email': argv[2]}
    email = urllib.parse.urlencode(emaildict)
    email = email.encode('ascii')
    request1 = urllib.request.Request(argv[1], email)
    with urllib.request.urlopen(request1) as response:
        page = response.read()
        print(page.decode('ascii'))
