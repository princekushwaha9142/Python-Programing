# Concatenation
a = [1, 2]
b = [3, 4]

print(a + b)   # [1, 2, 3, 4]

# Repetition
print([1, 2] * 3)

# Membership
nums = [10, 20, 30]

print(20 in nums)   # True
print(99 in nums)   # False


# append() 
nums = [10, 20]
nums.append(30)

print(nums)

# insert()
nums = [10, 20, 30]
nums.insert(1, 99)

print(nums)

# remove()
nums = [10, 20, 30]
nums.remove(20)

# pop() 

nums = [10, 20, 30]
nums.pop()

print(nums)

# sort()

nums = [5, 2, 8, 1]
nums.sort()

# reverse()
nums = [10, 20, 30]
nums.reverse()

# len() 
nums = [10, 20, 30]
print(len(nums))