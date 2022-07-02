a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
b = a.copy()

for k, v in b.items():
    if not v:
        del a[k]

print(a)