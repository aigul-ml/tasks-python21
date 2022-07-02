with open('task3.txt', 'w')as file1:
    for num in range(10):
        str_ =  str(num) + '*'
        file1.write(str_)

    file1.seek(0)

with open('task3.txt', 'r') as file2:
    print(file2.read())