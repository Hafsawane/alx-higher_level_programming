#!/usr/bin/python3
for char in range(ord('Z'), ord('A'), -1):
    letter = chr(char)
        if char % 2 == 0:
            letter = letter.upper()
        else:
            letter = letter.lower()
            print("{}".format(letter), end="")
print()                                                                                      
