#!/usr/bin/python3
"""
function that returns True if the object is an instanceof,
or if the object is an instance of a classs that inherited from,
the specifiend class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    returns true if the oject is an instanceof...
    """
    return True if isinstance(obj, a_class) else False
