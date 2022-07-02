with open('task5.txt') as file1:
    numbers = [int(line) for line in file1]

    file2 = open('task6.txt', 'w')
    file2.write(f"{min(numbers)}-{max(numbers)}")

    file2.close()