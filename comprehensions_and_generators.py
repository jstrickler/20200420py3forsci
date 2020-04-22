#!/usr/bin/env python

fruits = ["cherry", "apricot", "apple", "lemon"]

f1 = [f.upper() for f in fruits]  # list comprehension

print("f1: {}\n".format(f1))

f2 = (f.upper() for f in fruits)  # generator expression

print("f2: {}\n".format(f2))
print("list(f2): {}\n".format(list(f2)))

f2 = (f.upper() for f in fruits)  # generator expression
for fruit in f2:
    print(fruit)
print()

def upper_fruits():  # generator function
    for f in fruits:
        yield f.upper()  # yield the NEXT value


uf = upper_fruits()
for fruit in uf:  # run up to 'yield' and get value
    print(fruit)
print()


with open('DATA/mary.txt') as mary_in:
    for line in mary_in:
        print(line)
print()

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip()

mary_in = trimmed('DATA/mary.txt')
for line in mary_in:
    print(line)

def silly():
    yield "Python"
    yield "is"
    yield "the"
    yield "best"
    yield "language"

s = silly()
for m in s:
    print(m)
