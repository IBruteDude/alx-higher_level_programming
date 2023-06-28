#!/usr/bin/python3
"""a simple Square class module.

    Contents:
        The (Square) class definition.
        A basic test of its position property and my_print method.
"""


class Square:
    """a simple Square class with a side-length and position.
        Attributes:
            __size (int): the side-length of the square.
            __position (int, int): the position tuple of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """an error-checked initialiser for the two Square attributes.

        Args:
            size (int, optional): input value for side-length. Defaults to 0.

        Raises:
            ValueError: Only non-negative size's value is allowed.
            TypeError: the size variable has to be of type int.
        """
        if type(position) is tuple and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
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

    @property
    def position(self):
        """a position property for the Square.__position field.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """a position aware printer function for the square.
        """
        if self.size == 0:
            print()
        else:
            line = ('#' * self.size + '\n')
            if self.position[0] > 0 and not self.position[1] > 0:
                line = (' ' * self.position[0]) + line
            print("{}".format(line * self.size), end='')


if __name__ == '__main__':
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
