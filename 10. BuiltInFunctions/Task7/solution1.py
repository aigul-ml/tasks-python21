from functools import reduce

list_ = [5, 6, 7, 8]
result = reduce(lambda x, y: x * y, list_)
print(result)