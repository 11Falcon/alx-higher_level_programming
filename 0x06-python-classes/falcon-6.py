#!/usr/bin/python3
# falcon-6

class Square:
    """Define a class square """
    def __init__(self, size = 0, position = (0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)
    def position(self):
        return (self.__position)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("the size must be int")
        elif value < 0:
            raise TypeError("the size must => 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not insinstance(value, (int, int)):
            raise TypeError("the position must be a tuple of positive integers")
