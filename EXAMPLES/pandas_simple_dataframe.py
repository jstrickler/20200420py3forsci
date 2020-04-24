#!/usr/bin/env python
import pandas as pd
from printheader import print_header

cols = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']  # <1>
indices = ['a', 'b', 'c', 'd', 'e', 'f']  # <2>

values = [  # <3>
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    [600, 610, 620, 630, 640],
]
print_header('cols')
print(cols, '\n')

print_header('indices')
print(indices, '\n')

print_header('values')
print(values, '\n')

df = pd.DataFrame(values, index=indices, columns=cols)  # <4>
print_header('DataFrame df')
print(df, '\n')

print_header("df['gamma']")
print(df['gamma'])  # <5>

print_header("df['c':'c']")
print(df['c':'c'])
print()
columns_wanted = ['alpha', 'gamma', 'beta']
print(df[columns_wanted])

# df[NAME]   column NAME
# df[[NAME1, NAME2, ...]]   multiple columns
# df[ARRAY-LIKE]   multiple columns
# df[X:Y]    row slice from X to Y (Y exclusive if numeric, inclusive otherwise)




df *= 100

print(df)
