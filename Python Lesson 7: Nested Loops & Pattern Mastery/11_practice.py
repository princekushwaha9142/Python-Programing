#diamond pattern
rows = 5

# upper pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# lower inverted pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Logic:
# Total rows = 5
# Upper pyramid:
# In each row, spaces = total rows - current row number
# In each row, stars = 2 * current row number - 1
# Lower inverted pyramid:
# In each row, spaces = total rows - current row number
# In each row, stars = 2 * current row number - 1
