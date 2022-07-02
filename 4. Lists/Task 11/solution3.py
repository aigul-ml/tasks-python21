list_ = []
numbers = range(101)
i = 0

while i <= 100:
    if numbers[i] % 2 == 0:
        list_.append(numbers[i])
    i += 1

print(list_)