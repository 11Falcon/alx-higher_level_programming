#!/usr/bin/python3
"""class Student that defines a student by: (based on 10-student.py)"""
class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """initialise attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retreive attributes"""
        if attrs is None:
            return vars(self)
        the_dic = {}
        for att in attrs:
            if att in vars(self).keys():
                the_dic[att] = vars(self)[att]
        return the_dic

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for js in json:
            if js in vars(self).keys():
                setattr(self, js, json[js])
