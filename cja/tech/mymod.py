#!/usr/bin/env python
"""
Extraordinary demo module for the best students ever.

This demo module is full of silly functions
"""

COLORS = ['purple', 'green', 'pink']

def main():
    """
    Program entry point

    :return:
    """
    spam()
    ham()

def spam():
    """
    Spiced chopped pig parts

    :return:
    """
    print("Hello from spam()")


def ham():
    """
    Delicious leg of the swine.

    :return:
    """
    print("Hello from ham()")


def _eggs():  # "private"
    print("In eggs()...")

print("My name is", __name__)

if __name__ == '__main__':   # if run as script...
    main()

