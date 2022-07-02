cash = int(input())

if cash < 0:
    raise ValueError('Сумма не может быть отрицательной!')
else:
    print(int(cash))