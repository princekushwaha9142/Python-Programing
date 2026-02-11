nums = [10, 20, 30, 40, 50]

print(nums[0:3])   # [10, 20, 30]
print(nums[:2])    # [10, 20]
print(nums[::2])   # [10, 30, 50]

# Lists are MUTABLE 

# Unlike strings 

# Allowed:

a = [10, 20, 30]
a[0] = 99

print(a)   # [99, 20, 30]