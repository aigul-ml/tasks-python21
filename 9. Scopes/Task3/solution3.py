num = 3

def mul():
    global num
    num **= 2

for _ in range(3):
    mul()

print(num)