#!/usr/bin/python3
"""A module defining the BaseGeometry and Rectangle class and tests it"""


class BaseGeometry:
    """Empty BaseGeometry class"""
    def area(self):
        """An area method not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """Initialisation function for the Rectangle class"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """The string representation of Rectangle instances"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """The implemented area method for the Rectangle"""
        return self.__width * self.__height


if __name__ == '__main__':
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
