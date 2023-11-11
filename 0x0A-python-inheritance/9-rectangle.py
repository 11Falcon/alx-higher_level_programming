#!/usr/bin/python3
"""
Rectangle class that inherits from BaseGeometry
with __init__(self, width, height)
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectange inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ initialiser """
        self.__width = width
        self.__height = height
        super(). integer_validator("width", self.__width)
        super(). integer_validator("height", self.__height)

    def area(self):
        """method must be implementd"""
        return (self.__width * self.__height)

    def print(self):
        """print [Rectangle] <width>/<height>"""
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        """ return [Rectangle] <width>/<height>"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
