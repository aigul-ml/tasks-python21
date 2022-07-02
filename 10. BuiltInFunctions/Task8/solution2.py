list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
list2 = []
list3 = []

for x in list_:
    if x % 2 == 0:
        list2.append(x)
    else:
        list3.append(x)

result = f'even: {len(list2)}, odd: {len(list3)}'

print(result)