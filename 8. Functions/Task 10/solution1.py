def sum_digits(nums):
    result = 0
    for num in str(nums):
        result += int(num)
    
    return result

print(sum_digits(105))