#!/usr/bin/python3
"""A module defining the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Determines whether an object is of the type a_class or not"""
    return isinstance(obj, a_class)


if __name__ == '__main__':
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
