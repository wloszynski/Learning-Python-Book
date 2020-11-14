# decimal
d = 123
# hexa
h = 0x1F2
# octa
o = 0o71
# binary
b = 0b1010

print(d, h, o, b)

# complex numbers
print(complex(1, 2))

a = 3
b = 4

print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b ** 2)
print(2 + 4.0, 2.0 ** b)

print(b / (2.0 + a))

print('1' == 1)

# same as 1 == 2 and 2 < 3
print(1 == 2 < 3)

x = 2.2
y = 1.3

print(x / y)

print(x // y)

print(x % y)

# complex numbers
print(1J * 1j)

print(oct(64), hex(64), bin(64))

x = 1

print(x<<2)
print(x | 2)
print(x & 1)

x = 99
print(bin(x), x.bit_length(), len(bin(x)) - 2)