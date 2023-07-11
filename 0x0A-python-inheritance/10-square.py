#!/usr/bin/python3
"""A module defining the BaseGeometry, Rectangle and Square class and tests"""


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


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, size):
        """Initialisation function for the Square class"""
        self.__size = self.integer_validator("size", size)

    def area(self):
        """The implemented area method for the Square"""
        return self.__size ** 2

    def __str__(self):
        """The string representation of Rectangle instances"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)


if __name__ == '__main__':
    s = Square(13)

    print(s)
    print(s.area())
