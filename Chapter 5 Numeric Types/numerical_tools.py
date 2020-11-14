import math

print(math.pi, math.e)

print(math.sin(2 * math.pi / 180))

print(math.sqrt(144), math.sqrt(2))

print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)

print(abs(-42.0), sum((1, 2, 3, 4)))

print(min(3, 1, 2, 4), max(3, 1, 2, 4))

print(math.floor(2.567), math.floor(-2.567))

print(math.trunc(2.567), math.trunc(-2.567))

print(int(2.567), int(-2.567))

print(round(2.567), round(2.467), round(2.567,2))

print(math.sqrt(144), pow(144, .5), 144 ** .5)

import random

print(random.random())

print(random.randint(1, 10))

print(random.choice(['cat', 'dog', 'fish']))

suits = ['red', 'black', 'blue', 'yellow']
random.shuffle(suits)

print(suits)