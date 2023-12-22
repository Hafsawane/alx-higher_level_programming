#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if char != chr(ord(char) - 32):
            result += char
        else:
            result += chr(ord(char))
            print("{}".format(result))
