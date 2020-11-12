# sets 
X = set('spam')

print(X)

# decimals

print(1/3)

print(2/3 + 1/2)

import decimal

d = decimal.Decimal('3.141')
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))

# fractions

from fractions import Fraction

f = Fraction(2, 3)

print(f + 1)

L = [None] * 100
print(type(L))

print(type(type(L)))

if type(L) == type([]):
    print('yes')

if type(L) == list:
    print('yes')

if isinstance(L, list):
    print('yes')