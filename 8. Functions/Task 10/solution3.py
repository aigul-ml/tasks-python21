def sum_digits(nums):
    return sum(int(num) for num in str(nums))

print(sum_digits(105))