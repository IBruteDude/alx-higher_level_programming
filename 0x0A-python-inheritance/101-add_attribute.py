#!/usr/bin/python3
"""simple module for add_attribute function"""


def add_attribute(obj, name, value):
    """attempts to add attribute to an object"""
    if getattr(obj, name, None) is not None:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)


if __name__ == '__main__':
	pass

