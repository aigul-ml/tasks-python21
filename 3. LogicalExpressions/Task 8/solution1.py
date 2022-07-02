x = int(input())
y = int(input())

if x % y == 0:
    print('x делится на y')
    print('Частное: ' + str(x // y))
else:
    print('x не делится на y')
    print('Частное: ' + str(x // y))
    print('Остаток: ' + str(x % y))