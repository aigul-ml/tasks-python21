a = {'a': 1, 'b': 2, 'c': 1}
length = len(a)
i = 0

while i < length:
    a.popitem()
    i += 1

print(a)