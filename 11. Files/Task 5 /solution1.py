with open('task5.txt') as file1:
    numbers = []
    for line in file1:
        numbers.append(int(line))

    with open('task6.txt', 'w') as file2:
        file2.write(f"{min(numbers)}-{max(numbers)}")