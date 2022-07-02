from functools import reduce

def multiply_list(nums):
    total = reduce(lambda a, b: a * b, nums)
    return total

numbers = [1, 2, 3, 4, 5]

print(multiply_list(numbers))