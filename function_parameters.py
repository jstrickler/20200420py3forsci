#!/usr/bin/env python

def spam(a, b):  # 2 parameters require 2 arguments
    return a + b

print(spam(5, 10))
# print(spam(5))
# print(spam(5, 10, 15))

print(spam('foo', 'bar'))

def ham(a, *b):
    print("ham():", a, b)

def eggs(*a):
    print("eggs():", a)

ham(5)
ham(5, 10, 15)
ham('a', 4, 98, 103, "wombat", 3.1417)
print()

eggs(5)
eggs(5, 10, 15)
eggs('a', 4, 98, 103, "wombat", 3.1417)
eggs()
print()

def print_message(message, language="EN"):
    print(message, language)

print_message("Hello", "FR")
print_message("Hello", "ES")
print_message("Hello")


def cleanup(s):
    return ....


for old_str in spam:
    new_str = cleanup(old_str)
    print(old_str, new_str)
