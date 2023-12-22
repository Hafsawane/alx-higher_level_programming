#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = number % 10
    print("{:02d}\n".format(lastdigit))
    return lastdigit
