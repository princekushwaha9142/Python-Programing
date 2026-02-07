# continue — Skip Current Iteration
# Meaning

# continue skips the current loop step and moves to the next

# Example 1: Skip a number
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Example 2: Print only even numbers
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)