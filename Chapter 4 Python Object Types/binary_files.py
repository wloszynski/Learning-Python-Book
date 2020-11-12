import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)

print(packed)

file = open('Chapter 4 Python Object Types/data.bin', 'wb')

file.write(packed)

file.close()

data = open('Chapter 4 Python Object Types/data.bin', 'rb').read()

print(data)

print(data[4:8])

print(list(data))

struct.unpack('>i4sh', data)