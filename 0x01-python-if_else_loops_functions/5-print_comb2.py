#!/usr/bin/python3
message = ""
for i in range(99):
    message = ""
    if i < 10:
        message += '0'
    message += str(i)
    print(f"{message}, ", end="")
print("99")
