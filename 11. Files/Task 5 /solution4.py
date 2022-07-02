file1 = open('task5.txt')
numbers = [int(line) for line in file1]

file2 = open('task6.txt', 'w')
file2.write(f"{min(numbers)}-{max(numbers)}")

file1.close()
file2.close()