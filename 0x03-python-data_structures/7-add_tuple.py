#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]
    a = list(tuple_a) + result
    b = list(tuple_b) + result
    result[0] += a[0] + b[0]
    result[1] += a[1] + b[1]
    '''
    well f*** you we have no general solutions here
    '''
    # result = list([0] * max(len(list(tuple_a)), len(tuple_b)))
    # a = list(tuple_a)
    # b = list(tuple_b)
    # if len(a) < len(b):
    #     a += [0] * (len(b) - len(a))
    # if len(b) < len(a):
    #     b += [0] * (len(a) - len(b))
    # result = [a_i + b_i for a_i, b_i in zip(a, b)]
    return tuple(result)
