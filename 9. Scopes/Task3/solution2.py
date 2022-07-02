num = 3

def mul():
    global num
    num = pow(num, 2)

mul()
mul()
mul()
print(num)