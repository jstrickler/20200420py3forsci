#!/usr/bin/env python

people1 = ['Bob', 'Arthur', 'Carol', 'Mary', 'Ebenezer', 'Ahmed', 'Srini']
people2 = ['Arthur', 'Ahmed', 'Robin', 'Jackie', 'Kevin', 'Mary']

p1 = set(people1)
p2 = set(people2)
p1.add('Alice')
p1.add('Alice')
p1.add('Alice')
p1.add('Alice')
p1.add('Beatrice')

print(p1)
print(p2, '\n')

print("Common:", p1 & p2)  # intersection
print("NOT Common:", p1 ^ p2)  # Xor
print("All:", p1 | p2)  # union
print("Just p1:", p1 - p2)
print("Just p2:", p2 -p1)



