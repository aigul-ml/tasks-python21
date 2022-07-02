from functools import reduce

def sum_digits(nums):
    result = reduce(lambda a, b: int(a) + int(b), str(nums))
    return int(result)

print(sum_digits(105))