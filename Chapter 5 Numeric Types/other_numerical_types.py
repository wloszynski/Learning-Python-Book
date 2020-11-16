# print(0.1 + 0.1 + 0.1 - 0.3)

from decimal import Decimal

print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

from fractions import Fraction

print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))

print((2.5).as_integer_ratio())

f = 2.5

x = Fraction(1, 3)

z = Fraction(*f.as_integer_ratio())

print(z, x, z + x, float(x))

print(float(z), float(x + z), 17 / 6, Fraction.from_float(1.75))

print(Fraction(*(1.75).as_integer_ratio()))

