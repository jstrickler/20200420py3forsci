#!/usr/bin/env python
import sys

list1 = list()  # empty list
list2 = ['a', 'b', 'c']
list3 = []  # empty list
s = "fee:fi:fo:fum"
list4 = s.split(':')
print(list1, list2, list3, list4)

cities = ['Arlington', 'Falls Church', 'Clifton', 'Fairfax']

print(cities[0], cities[1], cities[3])
print(len(cities))
print(cities[-1])

cities.append("Manassas")
cities.append("Herndon")

print(cities)

cities.insert(0, 'Springfield')
cities.insert(3, 'Potomac Mills')

print(cities)

more_cities = ['Burke', 'Annandale', 'Chantilly']

cities.extend(more_cities)

print(cities)

del cities[6]  # remote the 7th element

print(cities)

cities.remove('Chantilly')

print(cities)

c = cities.pop()
print("c is", c)
print(cities)

c = cities.pop(3)
print("c is", c)
print(cities)

print("Clifton" in cities)
print("Front Royal" in cities)
print()

# iterables: list str bytes tuple set dict generator

for city in cities:
    #  city = next(cities)
    print(f"I would live in {city}")
print()

print(cities)
print(cities[0], cities[-1], cities[6], '\n')

print(cities[0:3])  # 0, 1, 2
print(cities[1:4])  # 1, 2, 3
print(cities[2:6])  # 2, 3, 4, 5

# S[START:STOP]   S[START:STOP:STEP]   S[START:]  S[:STOP]

print(cities[4:])
print(cities[1:])

print(sys.argv[1:])

for word in sys.argv[1:]:
    print("WORD:", word)

print(cities[-2:])

city = "Springfield"
print(city[:6])
print(city[6:])
print(city[3:6])



