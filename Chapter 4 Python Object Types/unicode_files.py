S = 'sp\xc4m'

print(S)
print(S[2])

file = open('Chapter 4 Python Object Types/unidata.txt', 'w', encoding='utf-8')

file.write(S)
file.close

text = open('Chapter 4 Python Object Types/unidata.txt', encoding='utf-8').read()

print(text)
print(len(text))

raw = open('Chapter 4 Python Object Types/unidata.txt', 'rb').read()

print(raw)

text.encode('utf-8')
