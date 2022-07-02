a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

for key in a.keys():
    a.update({key: a[key] / 5})

print(a)