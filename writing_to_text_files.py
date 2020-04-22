#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

with open('DATA/alice.txt') as alice_in:
    with open('lizard.txt', 'w') as lizard_out:
        with open('pig.txt', 'w') as pig_out:
            for line in alice_in:
                if "lizard" in line.lower():
                    lizard_out.write(line)
                if "pig" in line.lower():
                    pig_out.write(line)



