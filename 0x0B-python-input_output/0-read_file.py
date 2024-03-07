#!/usr/bin/python3
"""Read file in utf-8 encoding"""


def read_file(filename=""):
    """read the filename file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
