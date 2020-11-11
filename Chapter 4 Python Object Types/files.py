f = open('Chapter 4 Python Object Types/data.txt', 'w')
f.write('Hello,\n')
f.write('Adrian\n')
f.close


f = open('Chapter 4 Python Object Types/data.txt')
text = f.read()
print(text)

print(text.split())

for line in open('Chapter 4 Python Object Types/data.txt'): print(line)

print(dir(f))
print(help(f.seek))