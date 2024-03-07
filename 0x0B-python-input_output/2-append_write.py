#!/usr/bin/python3
"""append a string to a text file"""


def append_write(filename="", text=""):
    """append a string to a text file"""
    with open(filename, "a", encoding="utf-8") as File:
        File.append(text)
        return len(text)
