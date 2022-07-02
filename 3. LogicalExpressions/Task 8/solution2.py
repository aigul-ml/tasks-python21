x = int(input())
y = int(input())

if not x % y:
    print('x делится на y')
    print(f'Частное: {x // y}')
else:
    print('x не делится на y')
    print(f'Частное: {x // y}')
    print(f'Остаток: {x % y}')