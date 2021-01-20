#!/usr/bin/python3
"""Appends to files"""


def append_write(filename="", text=""):
    """append function"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
