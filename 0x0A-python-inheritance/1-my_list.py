#!/usr/bin/python3
"""A module for defining and testing MyList class"""


class MyList(list):
    """MyList class that inherits from list class"""
    def print_sorted(self):
        """Prints a MyList instance sorted"""
        print("{}".format(sorted(self)))


if __name__ == '__main__':
    lines = open("tests/1-my_list.txt").read().splitlines()
    for line in lines:
        MyList(eval(line)).print_sorted()
    # my_list = MyList()
    # my_list.append(1)
    # my_list.append(4)
    # my_list.append(2)
    # my_list.append(3)
    # my_list.append(5)
    # print(my_list)
    # my_list.print_sorted()
    # print(my_list)
