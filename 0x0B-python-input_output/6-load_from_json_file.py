#!/usr/bin/python3
"""creates object from a json file"""
import json


def load_from_json_file(filename):
    """json to obj"""
    with open(filename) as myFile:
        return json.loads(myFile.read())
