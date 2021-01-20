#!/usr/bin/python3
import json
"""Json to text file"""


def save_to_json_file(my_obj, filename):
    """Save to json file"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
