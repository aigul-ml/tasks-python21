set1 = {num for num in range(10)}
set2 = {num for num in range(10, 20)}
full_set = set1 | set2

if len(full_set) < 20:
    length = len(full_set)
    res = set1 & set2
    print(f'В этом сете было {len(res)} повторения, его длина составляет {length}')
else:
    print('Ваш объединенный сет полностью уникальный!')