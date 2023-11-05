#!/usr/bin/python3
#falcon-4.py
""" define Square class """
class Square:
    """ defining Square class instances """
    def __init__(self, size = 0):
        """size initialiser"""
        self.__size = size
    @property
    def size(self):
        """size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise TypeError("size must be => 0")
        self.__size = value
    
    def area(self):
        """ return the area of the square """
        return (self.__size ** 2)
