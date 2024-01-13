#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for number in my_list:
        my_list = reversed(my_list)
        print("{}".format(my_list))
