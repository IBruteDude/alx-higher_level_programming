#!/usr/bin/python3
"""Simple module for the class (Rectangle), and tests for it's functionality
"""


class Rectangle:
    """Rectangle class with basic properties and methods

        Attributes:
            width (int): the width of the rectangle. Defaults to 0.
            height (int): the height of the rectangle. Defaults to 0.
    """
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """initialisation function for a Rectangle instance

        Args:
            width (int, optional): the width of the rectangle. Defaults to 0.
            height (int, optional): the height of the rectangle. Defaults to 0.
        """
        Rectangle.number_of_instances += 1
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
        return ((Rectangle.print_symbol * self.width + '\n') * self.height)[:-1]

    def __del__(self):
        """Instance deleter special method
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """a static comparison method for rectangles

        Args:
            rect_1 (Rectangle): first input rectangle instance
            rect_2 (Rectangle): second input rectangle instance

        Raises:
            TypeError: if input isn't rectangles

        Returns:
            Rectangle: the bigger of the two rectangles or rect_1 if equal
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

if __name__ == '__main__':
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")
    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")
