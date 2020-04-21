#!/usr/bin/env python

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


cities = [("Herndon", "VA"), ("Tacoma", "MD"), ("Durham", "NC")]

print(cities[0], '\n')

for city in cities:
    print(city)
print()

# for var1, var2 in iterable_of_pairs
for city, state in cities:
    print(city, state)
print()


colors = ['orange', 'blue', 'green', 'yellow', 'chartreuse']

for color in colors:
    print(color)
print()


for i, color in enumerate(colors):
    print(i, color)
print()
print(list(enumerate(colors)), '\n')

e = enumerate(colors)
print(e)
for thing in e:
    print(thing)
print()








