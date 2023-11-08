#!/usr/bin/python3
"""
    Addition function for test
"""
def add_integer(a, b=98):
    """ Addition Function with test conditions"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
