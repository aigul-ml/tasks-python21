def multiply_list(nums):
    total = 1
    for num in nums:
        total *= num
        
    return total

numbers = [1, 2, 3, 4, 5, 6]

print(multiply_list(numbers))