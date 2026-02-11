# Reverse list using loop
nums = [10, 20, 30, 40]
reversed_nums = []
for i in range(len(nums)-1, -1, -1):
    reversed_nums.append(nums[i])
print(reversed_nums)
