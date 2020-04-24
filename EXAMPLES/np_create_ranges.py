#!/usr/bin/env python
import numpy as np

r1 = np.arange(50)  # <1>
print(r1)
print("size is", r1.size)  # <2>
print()

r2 = np.arange(5, 101, 5)  # <3>
print(r2)
print("size is", r2.size)
print()

r3 = np.arange(1.0, 25.0, .5)  # <4>
print(r3)
print("size is", r3.size)
print()

r4 = np.linspace(0.0, 16.0, 8)  # <5>
print(r4)
print("size is", r4.size)
print()



r1 = np.arange(50)  # <1>
print(r1)
print("size is", r1.size)  # <2>
print()

print(r1)
r1.shape = (5, 10)
print(r1)
r1.shape = (10, 5)
print(r1)
r1.shape = (5, 2, 5)
print(r1)
