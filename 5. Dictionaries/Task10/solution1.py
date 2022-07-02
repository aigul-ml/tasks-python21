a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

for k, v in list(a.items()):
    if v == None:
        a.pop(k)

print(a)