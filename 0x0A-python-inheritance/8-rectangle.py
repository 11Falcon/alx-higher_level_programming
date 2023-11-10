#!/usr/bin/python3
"""
class Rectangle that ingerits from BaseGeometry
instances: width and height
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ child class of  BaseGEometry"""
    def __init__(self, width, height):
        """initiate width and height"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
