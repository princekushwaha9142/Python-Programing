# Find the maximum value in a list

nums = [10, 20, 30, 40]
max_val = nums[0]
for n in nums:
    if n > max_val:
        max_val = n
print(max_val)