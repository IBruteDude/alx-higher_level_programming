#!/usr/bin/python3
"""a simple Square class module.

    Contents:
        The (Square) class definition.
        A basic test of its size attribute and errors.
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


if __name__ == '__main__':
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

        my_square_2 = Square(5)
        print("Area: {}".format(my_square_2.area()))
