#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle():
    """Class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing an instance of a rectangle class.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets/Sets width of rectangle

        Args:
            width (int): width of rectangle

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than zero.
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/Sets height of rectangle

        Args:
            height (int): height of rectangle

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than zero.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
