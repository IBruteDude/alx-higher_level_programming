#!/usr/bin/python3
"""A module defining the BaseGeometry class and tests it"""


class BaseGeometry:
    """Empty BaseGeometry class"""
    def area(self):
        """An area method not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a named integer argument correctly"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


if __name__ == '__main__':
    infile = open("tests/7-base_geometry.txt").read()
    lines = infile.replace(' ', '\n').splitlines()
    bg = BaseGeometry()
    for i in range(len(lines) // 2):
        try:
            bg.integer_validator(eval(lines[2 * i]), eval(lines[2 * i + 1]))
        except Exception as e:
            print("{}".format(e))
    # bg = BaseGeometry()

    # bg.integer_validator("my_int", 12)
    # bg.integer_validator("width", 89)

    # try:
    #     bg.integer_validator("name", "John")
    # except Exception as e:
    #     print("[{}] {}".format(e.__class__.__name__, e))

    # try:
    #     bg.integer_validator("age", 0)
    # except Exception as e:
    #     print("[{}] {}".format(e.__class__.__name__, e))

    # try:
    #     bg.integer_validator("distance", -4)
    # except Exception as e:
    #     print("[{}] {}".format(e.__class__.__name__, e))
