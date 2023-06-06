#!/usr/bin/python3
import os
str = bytes("and that piece of art is useful - Dora Korpar, 2015-10-19\n", "ascii")
os.write(2, str)
