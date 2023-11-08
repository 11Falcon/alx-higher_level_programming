#!/usr/bin/python3
"""
    Addition function for test
"""
def add_integer(a, b=98):
    """ Addition Function with test conditions"""
    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b,(int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
