# Hollow Square Pattern
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Logic:
# Total rows = 5
# Total columns = 5
# Print star if it's first or last row or first or last column else print space 
