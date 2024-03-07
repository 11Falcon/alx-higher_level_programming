#!/usr/bin/python3
"""
    write a string to a text file
    and return the number of caracters written
"""


def write_file(filename="", text=""):
    """write a string to a text file """
    with open(filename, "w", encoding="utf-8") as File:
        File.write(text)
        return (len(text))
