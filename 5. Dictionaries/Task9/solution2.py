a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
b = a.copy()

for k, v in a.items():
    if v % 2 == 0:
        b[k] = 2
    else:
        continue

print(b)