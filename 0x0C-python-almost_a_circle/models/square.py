#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialise arguments"""
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        se = "{} - {}".format(self.y, self.size)
        return "[Square] {} {}/{}".format(self.id, self.x, se)

