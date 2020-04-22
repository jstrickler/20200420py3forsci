#!/usr/bin/env python
# from cja/tech import mymod.py
from cja.tech import mymod

mymod.spam()
mymod.ham()

print(mymod.COLORS)

# don't call _eggs() -- it's _private
# mymod._eggs()
