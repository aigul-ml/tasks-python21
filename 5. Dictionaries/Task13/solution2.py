a = {'a': 1, 'b': 2, 'c': 3}
new_dict = {}

for k, v in a.items():
    new_dict[v] = k
print(new_dict)