#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list.clear()
    for i in range(idx):
        my_list.append(new_list[i])
    for i in range(idx + 1, len(new_list)):
        my_list.append(new_list[i])
    return my_list
