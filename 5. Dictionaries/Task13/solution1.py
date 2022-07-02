a = {'a': 1, 'b': 2, 'c': 3}

for k, v in list(a.items()):
    del a[k]
    a[v] = k

print(a)