a = 10
b = float(a)
c = str(a)
print(b, type(b))
print(c, type(c)) # TypeError: unsupported operand type(s) for +: 'float' and 'str'
d = a + b + c
print(d) 