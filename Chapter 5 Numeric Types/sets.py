print(set('spam'))

S = {'s', 'p', 'a', 'm'}
print(S)
S.add('monty')
print(S)

S1 = {1, 2, 3, 4}
print(S1 & {1, 3})
print({1, 5, 3, 6} | S1)
print(S1 - {1, 3, 4})
print(S1 > {1, 3})
print(S1 - {1, 2, 3, 4})

S = set()
S.add(1.23)
print(S)

print({1, 2, 3}.union([3, 4]))
print({1, 2, 3}.union({3, 4}))
print({1, 2, 3}.intersection((1, 3, 5)))
print({1, 2, 3}.issubset(range(-5, 5)))
