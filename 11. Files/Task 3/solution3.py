file = open('task3.txt', 'w+')

for num in range(10):
    str_ =  str(num) + '*'
    file.write(str_)
file.seek(0)

print(file.read())

file.close()