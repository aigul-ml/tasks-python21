inp1 = input()

try:
    numbers = []
    data = inp1.split()
    for number in data:
        numbers.append(int(number))
    print(numbers)
except:
    raise TypeError('Данный элемент не является числом!')