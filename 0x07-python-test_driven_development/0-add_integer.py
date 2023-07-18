#!/usr/bin/python3
"""Module for defining and testing the add_integer function
    Examples:
        >>> add_integer(1, 1)
        2
"""


def add_integer(a, b=98):
    """a type-safe function to add integers

    Args:
        a (int): first argument
        b (int, optional): second argument. Defaults to 98.

    Raises:
        TypeError: raised if type of a or b isn't int or float

    Returns:
        int: added value of a and b or a with 98
    """
    if type(a) is float or type(a) is int:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is float or type(b) is int:
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b


