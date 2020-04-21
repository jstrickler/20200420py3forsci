#!/usr/bin/env python

# int float bool complex

i1 = 100
i2 = 0x100   # hex
i3 = 0b100   # binary
i4 = 0o100   # octal

a = 23
b = 9

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # "true" division
print(a // b)   # floored (int) division
print(a ** b)   # exponentiation
print(a % b)   # modulo (remainder after division)

print(23.323 // 9.3902933)
print(-23.323 // 9.3902933)

x = 5
x *= 10   # x = x * 10
x /= 2    # x = x / 2
x -= 4    # x = x - 4
print(x)

#  x++ ++x x-- --x

a = "123"
b = "    456     "
c = "DeadBeef"

print(int(a) * 10)
print(int(b) * 10)
print(a * 10)

print(int(c, 16))

x = str(5.9)
y = str(43234)
print(type(x), x, type(y), y)

print(x, y)  # when you do this...
print(str(x), str(y))  # ...really getting this + '\n'
print()

print(x, y)
print(x)
print(y)

print(x, end='/')
print(y)

print(x, end='')
print(y)

print(x, y, sep=":")
print(x, y, sep=", ")

actor = "Chris Hemsworth"
city = "Sydney"

print(actor, "lives in", city)
print(f"{actor} lives in {city}")   #  f-string (formatted string)
print("{} lives in {}".format(actor, city))  # python 3 formatting
print("%s lives in %s" % (actor, city))   # legacy (python 2) formatting

value = 23 / 9
print(f"Value is {value:.2f}")
print("Value is {:.2f}".format(value))











