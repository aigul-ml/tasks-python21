nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
res = []

for i in range(len(nums)):
    if nums[i] >= 5:
        continue
    res.append(nums[i])

print(res)