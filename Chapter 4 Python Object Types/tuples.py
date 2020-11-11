T = (1, 2, 3, 4)
print(len(T))

print(T[0])
print(T.index(4))

# T[0] = 2 -> immutable

T = (2,) + T[1:]
print(T)

T = 'spam', 3.0, [11, 22, 33]
print(T[1])
print(T[2][1])

# T.append(4) -> immutable

