#!/usr/bin/python3
"""class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
_y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of
the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
"""
from models.base import Base


def is_int(name, value):
    """check if name is an integger"""
    if not isinstance(value, int):
        raise TypeError("{} must be an integer".format(name))


def is_positive(name, value):
    """check if name is positive"""
    if value <= 0:
        raise ValueError("{} must be > 0".format(name))


def is_under_zero(name, value):
    """check if name is under zero"""
    if value < 0:
        raise ValueError("{} must be >= 0".format(name))


class Rectangle(Base):
    """ the class Rectangle that inherits from Base:"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialise attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        se = "{} - {}/{}".format(self.y, self.width, self.height)
        return "[Rectangle] ({}) {}/{}".format(self.id, self.x, se)

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """__width setter"""
        is_int("width", value)
        is_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """__height setter"""
        is_int("height", value)
        is_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """__x setter"""
        is_int("x", value)
        is_under_zero("x", value)
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """__y setter"""
        is_int("y", value)
        is_under_zero("y", value)
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for s in range(self.y)]
        for i in range(self.height):
            [print(" ", end='') for s in range(self.x)]
            [print("#", end='') for j in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
