#!/usr/bin/python3
""" Square class inherits from Rectangle
with __init__()
and area()
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area of the Square"""
        return (self.__size ** 2)

    def __str__(self):
        return super().__str__()
