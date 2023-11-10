#!/usr/bin/python3
"""
function that returns True if the object is exactrly
an instance of a specifiend class otherwise False
Prototype: def is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    function that checks is the obj is an instance of a_class
    """
    return True if type(obj) is a_class else False
