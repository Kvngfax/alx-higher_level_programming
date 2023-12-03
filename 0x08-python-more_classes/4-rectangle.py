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

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle
        or 0 if width or height is zero"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the printable representation of the rectangle"""

        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return new_str
        for i in range(self.__height):
            for j in range(self.__width):
                new_str += "#"
            new_str += "\n"
        new_str = new_str[:-1]
        return new_str

    def __repr__(self):
        """Returns the string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"
