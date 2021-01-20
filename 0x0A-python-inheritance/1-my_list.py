#!/usr/bin/python3
"""inherits from list"""

class MyList(list):
    """New Class"""
    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
