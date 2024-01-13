#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        return None
    if not tuple_b:
        return None
    new_tuple = ()
    tuple_a = (0, 0)
    tuple_b = (0, 0)
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
