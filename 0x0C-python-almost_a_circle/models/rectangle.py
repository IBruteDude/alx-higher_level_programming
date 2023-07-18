#!/usr/bin/python3
"""Module for defining the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class that inherits from the Base class"""
    attr_tuple = ("id", "width", "height", "x", "y")

    def area(self):
        """calculate the area of the rectangle instance

        Returns:
            int: the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """renders the Rectangle positionally with '#' characters"""
        line = [' ' * self.x + '#' * self.width]
        shape_render = '\n' * self.y + '\n'.join(line * self.height)
        print(shape_render)

    def update(self, *args, **kwargs):
        """change specified attributes of the object

        Returns:
            Rectangle: the modified version
        """
        if len(args) == 0:
            for field, value in kwargs.items():
                setattr(self, field, value)
        else:
            for i in range(len(args)):
                setattr(self, __class__.attr_tuple[i], args[i])
        return self

    def to_dictionary(self):
        """convert the Rectangle object into a dict representation

        Returns:
            dict[int]: the dict representation of the object attributes
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises the rectangle instance private attributes

        Args:
            width (int): The specified Rectangle width
            height (int): The specified Rectangle height
            x (int, optional): The Rectangle's x coordinate. Defaults to 0.
            y (int, optional): The Rectangle's y coordinate. Defaults to 0.
            id (int, optional): The Rectangle instance's id. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """The string formatted representation of the Rectangle instance"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    @property
    def width(self):
        """instance property for private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """instance property for private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """instance property for private attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """instance property for private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)
    r2 = Rectangle(2, 10)
    print(r2.id)
    r3 = Rectangle(10, 2, 0, 0, 12)

    print('-' * 73)

    r1 = Rectangle(4, 6)
    r1.display()
    print("---")
    r1 = Rectangle(2, 2)
    r1.display()

    print('-' * 73)

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

    print('-' * 73)

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

    print('-' * 73)

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

    print('-' * 73)

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

    print('-' * 73)

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

    print('-' * 73)

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

    print('-' * 73)

    list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

    print('-' * 73)

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
