#!/usr/bin/python3
"""Simple module for the class (Rectangle), and tests for it's functionality
"""


class Rectangle:
    """Rectangle class with basic properties and methods

        Attributes:
            width (int): the width of the rectangle. Defaults to 0.
            height (int): the height of the rectangle. Defaults to 0.
    """
    def __init__(self, width=0, height=0):
        """initialisation function for a Rectangle instance

        Args:
            width (int, optional): the width of the rectangle. Defaults to 0.
            height (int, optional): the height of the rectangle. Defaults to 0.

        Raises:
            TypeError: raised if width or height are not integers
            ValueError: raised if the value of width or height is negative
        """
        self.width = width
        self.height = height

    def __repr__(self):
        """the formal string representation of the rectangle

        Returns:
            str: string representation of the Rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __str__(self):
        """the informal string representation of the rectangle

        Returns:
            str: string representation of the Rectangle
        """
        return (('#' * self.width + '\n') * self.height)[:-1]

    @property
    def width(self):
        """a width property for the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a height property for the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """a method for calculating area

        Returns:
            int: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """a method for calculating area

        Returns:
            int: perimeter of the rectangle (0 if one dimension is 0)
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
