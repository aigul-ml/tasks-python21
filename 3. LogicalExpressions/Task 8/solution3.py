x = int(input())
y = int(input())

if x % y != 0:
    print(f"""x не делится на y
Частное: {x // y}
Остаток: {x % y}""")
else:
    print(f"""x делится на y
Частное: {x // y}""")