number = int(input())

if not number:
    print('zero')
elif number < 0:
    print('negative')
else:
    print('positive')

# В первом условии мы используем логический оператор not, так как цифра 0 приравнивается логическому значению False, оператор not превращает False в True.