#!/usr/bin/env python

d1 = dict()
capitals = {'NC': 'Raleigh', 'MD': 'Annapolis', 'VA': 'Richmond'}
d2 = {}
d3 = dict(red=22, green=45, blue=98)

print(capitals)
capitals['NJ'] = 'Trenton'
capitals['WV'] = "Charleston"
print(capitals)
del capitals['WV']
print(capitals)
print()

print(capitals['NC'])
print(capitals.get('WV'))
print(capitals.get('WV', 'NO CAPITAL'))

print(capitals.setdefault('NC', 'Wombat'))
print(capitals.setdefault('WV', 'Charleston'))
print(capitals)
print()

for state, capital in capitals.items():
    print(state, capital)
print()

counts = {}
with open('DATA/words.txt') as words_in:
    for line in words_in:
        first_letter = line[0]

        if first_letter not in counts:
            counts[first_letter] = 0

        counts[first_letter] = counts[first_letter] + 1  # increment count
        #  counts[first_letter] += 1

for letter, count in counts.items():
    print(letter, count)
print('-' * 60)



