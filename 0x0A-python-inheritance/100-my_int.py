#!/usr/bin/python3
"""A simple module for defining inverted equality int"""


class MyInt(int):
    """Inverted equality int class"""
    def __eq__(self, other):
        """Inverted equality"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Inverted inequality"""
        return int.__eq__(self, other)


if __name__ == '__main__':
	my_i = MyInt(3)
	print(my_i)
	print(my_i == 3)
	print(my_i != 3)
