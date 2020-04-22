#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0: {}\n".format(f0))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n0 = sorted(nums)
print("n0: {}\n".format(n0))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)

n1 = sorted(nums, reverse=True)
print("n1: {}\n".format(n1))

def ignore_case(f):
    return f.lower()

f1 = sorted(fruits, key=ignore_case)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=len)
print("f2: {}\n".format(f2))

def by_len_and_name(fruit):
    return len(fruit), fruit.lower()

f3 = sorted(fruits, key=by_len_and_name)
print("f3: {}\n".format(f3))

def by_dob(p):
    return p[-1]  # return last element of person

for person in sorted(people, key=by_dob):
    print(person)
print()

for person in sorted(people, key=lambda p: p[-1]):
    print(person)
print()



for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print()
