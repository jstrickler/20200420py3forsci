#!/usr/bin/env python
import sys

def c2f(celsius):
    return ((9 * celsius) / 5) + 32

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            c = float(sys.argv[1])
        except Exception as err:
            print(err)
        else:
            print(c2f(c))
    else:
        print("Please specify a numeric temperature in C")
