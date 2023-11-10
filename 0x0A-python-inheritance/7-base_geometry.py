#!/usr/bin/python3
"""
BaseGeometry class
public instance method: def area(self)
public instance method def integer_validator(self, name, value)
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        public instance method
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        value validation
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
