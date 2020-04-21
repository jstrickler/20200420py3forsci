#!/usr/bin/env python


while True:
    name = input("What is your name? ")
    if name == 'q':
        break    # exit loop NOW
    if name == '':
        continue  # go to top
    print(f"Welcome, {name}")

