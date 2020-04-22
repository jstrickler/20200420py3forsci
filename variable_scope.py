#!/usr/bin/env python

x = 100  # GLOBAL variable


def spam():
    y = 42  # LOCAL variable
    print("in spam(): x is", x)
    print("in spam(): y is", y)

spam()

print("in main: x is", x)
# print("in main: y is", y)  y is local to spam()



