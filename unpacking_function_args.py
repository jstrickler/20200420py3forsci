#!/usr/bin/env python


def spam(a, b, c):
    print(a)
    print(b)
    print(c)
    print()


spam(1, 2, 3)
spam('alpha', 'beta', 'gamma')

data = ['a', 'b', 'c']

spam(*data)
spam(data[0], data[1], data[2])

stuff = 'xyz'

spam(*stuff)
