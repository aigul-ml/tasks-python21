file = open('task1.txt', 'r')

lines = file.readlines(9)
for line in lines:
    print(line)

file.close()