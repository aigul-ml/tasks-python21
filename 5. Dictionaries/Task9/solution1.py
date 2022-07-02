a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
b = {}

for k, v in a.items():
    if v % 2 == 0:
        b[k] = 2
    else:
        b[k] = v

print(b)