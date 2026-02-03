#hollow pyramid pattern
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")

    for j in range(1, 2 * i):
        if i == rows or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Logic:
# Total rows = 5
# In each row, spaces = total rows - current row number
# In each row, stars at the borders and bottom row = 2 * current row number - 1
# In each row, spaces in between = (2 * current row number - 1) - 2
