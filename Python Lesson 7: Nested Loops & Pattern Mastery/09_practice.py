#pyramid star pattern
rows = 5

for i in range(1, rows + 1):
    # print spaces
    for space in range(rows - i):
        print(" ", end="")
    
    # print stars
    for star in range(2 * i - 1):
        print("*", end="")
    
    print()

# Logic:
# Total rows = 5
# In each row, spaces = total rows - current row number
# In each row, stars = 2 * current row number - 1