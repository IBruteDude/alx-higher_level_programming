#!/usr/bin/python3
"""Module for defining the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a Square class that inherits from the Rectangle class

    Attributes:
        id(int): the id of the instance
    """
    attr_tuple = ("id", "size", "x", "y")

    def to_dictionary(self):
        """The dictionary representation of the object

        Returns:
            dict: a dictionary representation of the object's attributes
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }

    def __init__(self, size, x=0, y=0, id=None):
        """the constructor for Square instances

        Args:
            size (int): the size of the Square
            x (int, optional): the Square's x-coordinate. Defaults to 0.
            y (int, optional): the Square's y-coordinate. Defaults to 0.
            id (int, optional): the id for Square instances. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation of Square class instances

        Returns:
            str: the string representation of the Square instance
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """The Square size property."""
        return self.width

    @size.setter
    def size(self, value):
        self.height = self.width = value


if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

    print('-' * 73)

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print('-' * 73)

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)

    print('-' * 73)

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)

    print('-' * 73)

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))
