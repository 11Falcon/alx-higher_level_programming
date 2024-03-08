#!/usr/bin/python3
"""
    Creating an obj from json file
"""
import json


def load_from_json_file(filename):
    """creting an obj from a json file"""
    with open(filename, "r", encoding="utf-8") as File:
        return json.loads(File.read())
