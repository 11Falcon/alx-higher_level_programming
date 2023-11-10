#!/usr/bin/python3
"""
function that returns True if the object is an instance of
a class that inhirited (derictly or indirectly) from
the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """
    does the obj inherits from a_class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
