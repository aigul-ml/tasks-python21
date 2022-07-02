file1 = open('task3.txt', 'w')

for num in range(10):
    str_ =  str(num) + '*'
    file1.write(str_)
file1.seek(0)

file2 = open('task3.txt', 'r')

print(file2.read())

file1.close()
file2.close()