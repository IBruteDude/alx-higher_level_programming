#!/usr/bin/python3
"""A module defining the inherits_from function"""


def inherits_from(obj, a_class):
    """ Determine if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """
    return type(obj) is not a_class and isinstance(obj, a_class)


if __name__ == '__main__':
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
