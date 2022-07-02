a = {'a': 3, 'b': 2}
total = 0
i = 0

while i < len(a):
    total += list(a.values())[i]
    i += 1

print(total)