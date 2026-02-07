# break — Stop the Loop Immediately

# Meaning

# break exits the loop completely, no more iterations

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Example 2: Find the first odd number in a list
nums = [2, 4, 6, 7, 8]

for n in nums:
    if n % 2 != 0:
        print("First odd number:", n)
        break