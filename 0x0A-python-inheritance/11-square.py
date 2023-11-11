#!/usr/bin/python3
"""
 Square that inherits from rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ inherits from Rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str function that returns the next thing"""
        return str("[Square] {}/{}".format(self.__size, self.__size))
    def area(self):
        """ return the area of the square"""
        return self.__size ** 2
