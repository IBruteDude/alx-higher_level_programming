#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        res_list = [0] * list_length
        for i in range(list_length):
            try:
                res_list[i] = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return res_list


if __name__ == '__main__':
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
