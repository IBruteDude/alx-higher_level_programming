#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100 + 1):
        message = ""
        if i % 3 == 0:
            message += "Fizz"
        if i % 5 == 0:
            message += "Buzz"
        if message == "":
            message = str(i)
        print(f"{message} ", end='')
