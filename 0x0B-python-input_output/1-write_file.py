#!/usr/bin/python3
"""Writes to file"""


def write_file(filename="", text=""):
    """File write"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
