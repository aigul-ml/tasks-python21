a = {'a': 1, 'b': 2, 'c': 1}

for k in list(a.keys()):
    a.pop(k)

print(a)