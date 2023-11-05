#!/urs/bin/python3

class Square:
    """ Define a class square """
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise TypeError("size must be => 0")
        self.__size = size
