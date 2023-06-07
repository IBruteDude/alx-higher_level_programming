#!/usr/bin/python3
def print_last_digit(number):
    mod = number % 10
    if number < 0:
        mod = 10 - mod
    print(f"{mod}", end='')
    return mod
