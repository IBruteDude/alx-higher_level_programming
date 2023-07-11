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


if __name__ == '__main__':
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
