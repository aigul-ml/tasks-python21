result = 0

def pow_first(x, y):
    global result
    result = x**y

def pow_second(z):
    global result
    result = result % z

pow_first(2, 3)
pow_second(3)
print(result) 