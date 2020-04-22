#!/usr/bin/env python

class Animal:
    def move(self):
        print("moving...")


class Dog(Animal):
    def __init__(self, bark_type):
        self.bark_type = bark_type

    def bark(self):  # method
        print(f"{self.bark_type}! {self.bark_type}!")

    def bark_loud(self):
        print(f"{self.bark_type.upper()}! {self.bark_type.upper()}!")

d1 = Dog('woof')  # create instance

d1.bark()   # call method  Dog.bark(d1)
d1.move()

d2 = Dog('yip')

d2.bark()   # Dog.bark(d2)
d2.bark_loud()

d3 = Dog('arf')
d3.bark()


# f = MyFileFormat(file_name)
#
# c = Config(config_file)
#
# db = MyDBModule.connect(hostname, database, username, password)
#



