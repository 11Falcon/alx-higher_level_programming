#!/usr/bin/python3
"""returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """"
        returns an obj represented by a json string
    """
    return (json.loads(my_str))
