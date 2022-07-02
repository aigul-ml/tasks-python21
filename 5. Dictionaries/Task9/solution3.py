from copy import deepcopy

a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
b = deepcopy(a)

for k, v in a.items():
    b[k] = 2 if not v % 2 else v

print(b)