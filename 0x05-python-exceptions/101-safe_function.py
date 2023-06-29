#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pass
