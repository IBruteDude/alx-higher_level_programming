#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    if length == 0:
        return []
    bool_list = [False] * length
    for i in range(length):
        if my_list[i] % 2 == 0:
            bool_list[i] = True
    return bool_list
