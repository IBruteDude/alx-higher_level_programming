#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) and ord(i) <= ord('z'):
            print("{}".format(chr(ord(i) + 65 - 97)), end='', flush=True)
        else:
            print("{}".format(i), end='')
    print("")


uppercase("das")