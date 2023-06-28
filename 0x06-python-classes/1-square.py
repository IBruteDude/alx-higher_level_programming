#!/usr/bin/python3
"""a simple Square class module.

    contains the class (Square) definition, with a basic test of its attribute
"""


class Square:
    """a simple Square class with a side-length.

    Attributes:
        __size (int): the side-length of the square.
    """
    def __init__(self, size):
        """a non error-checked initialiser function for the __size attribute.

        Args:
            size (int): the input side-length
        """
        self.__size = size


if __name__ == '__main__':
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
    pass
