#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    if number == 1:
        print("1 argument :", end="\n")
    elif number == 0:
        print("0 arguments.", end="\n")
    else:
        print("{} arguments :".format(number), end="\n")

    for i in number:
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
