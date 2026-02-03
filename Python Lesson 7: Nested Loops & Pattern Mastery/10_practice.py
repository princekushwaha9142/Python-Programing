#inverted pyramid pattern
rows = 5

for i in range(rows):
    print(" " * i + "*" * (2 * (rows - i) - 1))

# Logic:
# Total rows = 5
# In each row, spaces = row number
# In each row, stars = 2 * (total rows - row number) -