list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

list2 = list(filter(lambda x: x % 2 == 0, list_))
list3 = list(filter(lambda x: x % 2 > 0, list_))

result = f'even: {len(list2)}, odd: {len(list3)}'
print(result)