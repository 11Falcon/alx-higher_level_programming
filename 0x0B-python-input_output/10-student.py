#!/usr/bin/python3
"""Student class"""


class Student:
    """defined by :
    first_name:str
    last_name: str
    age:int"""
    def __init__(self, first_name, last_name, age):
        """initialise attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        the_dic = {}
        for at in attrs:
            if at in vars(self).keys():
                the_dic[at] = vars(self)[at]
        return the_dic
