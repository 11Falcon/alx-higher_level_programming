#!/usr/bin/python3
"""
Class MyInt that inherits int
MyInt is a rebel
"""


class MyInt(int):
    """
    rebel int class
    == and != operators are inverted
    """
    def __eq__(self, obj):
        """Equality turns to inequality"""
        return super().__ne__(obj)

    def __ne__(self, obj):
        """Inequality turns to Equality"""
        return super().__eq__(obj)
