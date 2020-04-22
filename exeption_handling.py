#!/usr/bin/env python

#  Base error:  Exception

try:
    with open("wombats.txt") as wombats_in:
        pass
except FileNotFoundError as err:
    print(err)


data = [5, 8, -4, 10]

try:
    print(data[10])
except IndexError as err:
    print(err)


values = 5, 8.1, 2.37, 0.0, "123", 17.3, 4.13

for v in values:
    try:
        result = 29 / v
    except ZeroDivisionError as err:  # if try: block raised ZDE....
        print(err)
    except (TypeError, ValueError) as err:  # if try: block raised TE or VE
        print(err)
    else:
        print(result)


def spam(a, b):  # 2 parameters require 2 arguments
    try:
        result = a + b
    except TypeError:
        return None
    else:
        return result



print(spam(5, 10))
print(spam("a", "b"))
print(spam(5, 'b'))
