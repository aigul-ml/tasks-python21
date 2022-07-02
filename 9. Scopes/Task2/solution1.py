x = 'Я глобальная переменная!'
print(x)

def my_func():
    global x
    x = 'Я могу изменяться'
    
my_func()
print(x)
print(globals())