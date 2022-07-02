nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
res = []
i = 0

while i < len(nums):
    res += [nums[i]] if nums[i] < 5 else []
    i += 1

print(res)