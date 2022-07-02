inp1 = input()

try:
    numbers = [int(num) for num in list(inp1.split())]
    print(numbers)
except:
    raise TypeError('Данный элемент не является числом!')