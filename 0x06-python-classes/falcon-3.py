#!/usr/bin/python3
""" define the class square """
class Square:
    def __init__(self, size = 0):
        """initialize self instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be => 0")
        self.__size = size

    def area(self):
        return (self.__size**2)
