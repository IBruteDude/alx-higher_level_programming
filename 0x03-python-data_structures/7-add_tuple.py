#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = list([0] * max(len(list(tuple_a)), len(tuple_b)))
    a = list(tuple_a)
    b = list(tuple_b)
    if len(a) < len(b):
        a += [0] * (len(b) - len(a))
    if len(b) < len(a):
        b += [0] * (len(a) - len(b))
    result = [a_i + b_i for a_i, b_i in zip(a, b)]
    return tuple(result)
