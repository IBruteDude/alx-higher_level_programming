#!/usr/bin/python3
"""simple module for add_attribute function"""


def add_attribute(obj, name, value):
    """attempts to add attribute to an object"""
    if not hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)


class MyClass():
    pass
if __name__ == '__main__':
    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)
    
    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
