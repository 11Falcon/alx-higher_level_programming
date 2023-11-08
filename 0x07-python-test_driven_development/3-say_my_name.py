#!/usr/bin/python3
"""
python function
returns: My name is <first name> <last name>
takes as input: first_name and last_name that must be strings
"""


def say_my_name(first_name, last_name=""):
    """
    say my name function
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is " + first_name + " " + last_name)
