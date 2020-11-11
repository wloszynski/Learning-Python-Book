D = {'food': 'spam', 'amount': 4, 'color': 'pink'}

print(D['food'])
D['amount'] += 1

print(D)


D = {}

D['name'] = 'Adrian'
D['job'] = 'Data Scientist'
D['age'] = 23

print(D)

bob1 = dict(name='Adrian', job='Data Scientist', age=23)
bob2 = dict(zip(['name', 'job', 'age'], ['Adrian', 'Data Scientist', 23]))

print(bob1)
print(bob2)

rec = {'personal data': {'name': 'Adrian', 'surname': 'Wloszynski'},
       'job': ['Data Scientist', 'engineer'],
       'age': 23.5}


print(rec)
print(rec['personal data'])
print(rec['personal data']['surname'])

rec['job'].append('hitchhiker')
print(rec)

if not 'f' in D:
    print('Doesn\'t exist')

value = D.get('x', 0)
print(value)

value = D['x'] if 'x' in D else 0
print(value)


Ks  = list(D.keys())
print(Ks)

Ks.sort()
print(Ks)

for key in Ks:
    print(key, '=>', D[key])


for key in sorted(D):
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())

x = 4
while x > 0:
    print('Spam!' * x)
    x -= 1

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)

print(squares)