#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for i in str:
        if ord('a') <= ord(i) and ord(i) <= ord('z'):
            newstr += chr(ord(i) + 65 - 97)
        else:
            newstr += i
    print("{}".format(newstr))
