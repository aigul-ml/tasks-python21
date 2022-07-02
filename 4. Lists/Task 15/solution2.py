list_ = []
numbers = range(54, 9184)
i = 0

while i < len(numbers):
    if numbers[i] % 5 == 0:
        list_.append(numbers[i])
    i += 1

print(list_)