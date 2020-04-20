#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # RAW string


print(len(s1))
print("It's a Python thing")
print('It is a "Python" thing')
print("""It's a "Python" thing""")

print("Whitespace:\n\r\f\b\t")

query = """
select * 
from customers
where cust_id = '1234'
order by state desc
"""

