#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = list([0] * max(len(list(tuple_a)), len(tuple_b)))
    a = result.copy()
    b = result.copy()
    for i in range(tuple_a.count()):
        a[i] = tuple_a.index(i)
    for i in range(tuple_b.count()):
        b[i] = tuple_b.index(i)
    result = [a_i + b_i for a_i, b_i in zip(a, b)]
    return tuple(result)
