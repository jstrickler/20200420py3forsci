#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'eggs', 'toast', 'bacon',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs']

good_food = [f for f in food if f != 'spam']
print("good_food: {}\n".format(good_food))

seen = set()
good_food2 = [f for f in food if (f not in seen and (1, seen.add(f))) and (f != 'spam')]
print(good_food2)

seen = set()
good_food_gen = (f for f in food if (f not in seen and (1, seen.add(f))) and (f != 'spam'))

print("good_food_gen: {}\n".format(good_food_gen))

for food in good_food_gen:
    print(food)

fruit_gen = (f.upper() for f in fruits)
print("fruit_gen: {}\n".format(fruit_gen))
for fruit in fruit_gen:
    print(fruit)
