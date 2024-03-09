#!/usr/bin/python3
"""class student"""


class Student:
    """a student instance containing his info"""
    def __init__(self, first_name, last_name, age):
        """initialise attributes"""
        self.first_name = first_name
        self.lat_name = last_name
        self.age = age

    def to_json(self):
        """retreive a dic"""
        return self.__dict__
