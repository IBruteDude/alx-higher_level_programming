#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
if mod == 0:
    message = f"Last digit of {number} is 0 and is "
elif number < 0:
    message = f"Last digit of {number} is {mod - 10} and is "
else:
    message = f"Last digit of {number} is {mod} and is "

if mod == 0:
    message += "0"
elif mod < 6:
    message += "less than 6 and not 0"
else:
    message += "greater than 5"
print(message)
