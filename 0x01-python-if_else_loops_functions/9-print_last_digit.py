#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = abs(number) % 10
    if number < 0:
        lastdigit = - lastdigit
        return lastdigit
    else:
        return lastdigit
    print("{:02d}".format(lastdigit))
