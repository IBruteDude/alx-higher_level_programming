#!/usr/bin/python3
def add_attribute(obj, name, value):
    if getattr(obj, name) is not None:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
    

if __name__ == '__main__':
	pass

