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

actor = "Chris Hemsworth"

print(len(actor))

#  function(S)   # built-in functions
#  S.method()    # string methods

print(actor.upper())
print(actor)
actor_upper = actor.upper()
print(actor_upper)

# help(str)
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))

data = "abc;5;Wichita;KS"
fields = data.split(';')  # str -> list
print(fields)

new_data = "|".join(fields)   # list (or other iterable) -> str
print(new_data)

s = "     All my exes live in Texas     "
print("|" + s.lstrip() + "|")  # strips  ' '  \t \n \r \f \b
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xyxxyyxxxyyyAll my exes live in Texasyxyyxxyyyxxx"
print("|" + s.lstrip('xy') + "|")  # strips  x or y
print("|" + s.rstrip('xy') + "|")
print("|" + s.strip('xy') + "|")
print()

print(actor)
print(actor.find("Hem"))
print(actor.find("worth"))
print(actor.find("Liam"))

print("Chris" in actor)
print("Liam" in actor)











