def multiply_list(nums):
    total = 1
    i = 0
    while i < len(nums):
        total = total * nums[i]
        i += 1
        
    return total

numbers = [1, 2, 3, 4, 5, 6]

print(multiply_list(numbers))