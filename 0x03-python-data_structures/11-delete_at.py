#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0 or idx == 0:
        return None

    if idx < 0 or idx is None:
        return my_list
    else:
        del my_list[idx]
        return my_list