a = {'apple': 2, 'orange': 5, 'banana': 10}
b = a.copy()

for k, v in b.items():
    if not v % 2:
        del a[k]
        
print(a)