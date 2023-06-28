#!/usr/bin/python3
"""a simple Square class module.

    Contents:
        The (Square) class definition.
        A basic test of its size property.
"""


class Square:
    """a simple Square class with a side-length field and an area method.

        Attributes:
            __size (int): the side-length of the square.
    """
    def __init__(self, size=0):
        """an error-checked initialiser for the Square.__size attribute.

        Args:
            size (int, optional): input value for side-length. Defaults to 0.

        Raises:
            ValueError: Only non-negative size's value is allowed.
            TypeError: the size variable has to be of type int.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculate the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """a size property for the Square.__size field.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")


if __name__ == '__main__':
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
