file1 = open('task5.txt')
numbers = []

for line in file1:
    numbers.append(int(line))

file2 = open('task6.txt', 'w')

print(file2.write(f"{min(numbers)}-{max(numbers)}"))

file1.close()
file2.close()