L = [123, 'spam', 1.23]

print(len(L))

print(L[0])
print(L[:-1])
print(L + [4, 5, 6])
print(L*2)
print(L)

L.append('NI')
print(L)
L.pop()
print(L)
# print(help(list.pop))

M = ['bb', 'aa', 'cc']
# print(M.sort())
M.sort()
print(M)
M.reverse()
print(M)
# print(M[88])

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(M)
print(M[1])
print(M[1][2])

col2 = [row[1] for row in M]
# return row[1] for each row in M in new list
print(col2)

print([row[1] for row in M if row[1] % 2 == 0])