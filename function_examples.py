#!/usr/bin/env python

def get_message():
    return "HELLO"

m = get_message()

print(m)

def print_message():
    m = get_message()
    print(m)

# two worlds of functions:
#  1. business logic
#  2. user interface logic  (AKA GUI AKA CLI AKA WI AKA UX)


def rectangle_area(height, width):
    return height * width

def show_area():
    raw_height = input("Enter height: ")
    raw_width = input("Enter width: ")
    h = float(raw_height)
    w = float(raw_width)
    area = rectangle_area(h, w)
    print(f"The area of a {h}x{w} rectangle is {area}")

show_area()


def print_area(height, width):
    area = rectangle_area(height, width)
    print("area is ", area)

x = print_area(5, 5)
y = print_area(7, 14)
print(x, y)

def spam():
    print("Hello")

x = spam()
print("x is:", x)
print("calling spam():", spam())









