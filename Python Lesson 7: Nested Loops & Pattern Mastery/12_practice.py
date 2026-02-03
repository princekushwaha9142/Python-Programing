#pyramid number pattern
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
    
# Logic:
# Total rows = 5
# In each row, spaces = total rows - current row number
# In each row, increasing numbers from 1 to current row number
# In each row, decreasing numbers from current row number - 1 to 1
             