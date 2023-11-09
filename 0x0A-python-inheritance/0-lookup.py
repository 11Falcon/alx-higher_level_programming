#!/usr/bin/python3
"""
 function that returns the list of available attributes
 and methods of an object
 Prototype: def lookup(obj):
 Returns a list object
"""


def lookup(obj):
    """ the list of available attributes"""
    return (dir(obj))
