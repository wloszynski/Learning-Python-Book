S = 'Spam'

print(S[0])
print(S[-1])
print(S[1:3])
print(S[1:])
print(S)

print(S[::2])
# print(S[START:END:ITERATION])

print(S*8)


S = 'duck'

L = list(S)

print(L)

L[0] = 'h'

print(''.join(L))

B = bytearray(b'mini')
B.extend(b'marathon')

print(B)

print(B.decode())


S = 'Spam'

print(S.find('am'))
print(S.replace('am','XYZ'))
print(S)

line='aaa,bbb,cccccc,ddd'
print(line.split(','))

print(S.upper())
print(S.isalpha())

line = 'aaa,bbbb,cccccc,dd\n'
print(line)
line = line.rstrip()
print(line)

print(line.rstrip().split(','))

# print('%s, eggs and, %s'('"spam","SPAM!"'))
