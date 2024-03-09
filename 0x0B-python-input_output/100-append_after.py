#!/usr/bin/python3
"""function that inserts a line of text to a file,
after each line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """inserting a line of text to a file
    after each line containing a specific string"""
    with open(filename, "w+", encoding="utf-8") as File:
        line = File.readline()
        while line != "":
            if search_string in line:
                File.write(new_string)
            line = File.readline()
