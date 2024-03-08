#!/usr/bin/python3
"""
    write an obj to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """ save an obj to a text file"""
    with open(filename, "w", encoding="utf-8") as File:
        File.write(json.dumps(my_obj))
