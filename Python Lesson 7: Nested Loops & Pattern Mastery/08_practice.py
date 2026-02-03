for i in range(5):
    # print spaces
    for space in range(i):
        print(" ", end="")
    
    # print stars
    for star in range(5 - i):
        print("*", end="")
    
    print()
    
# Logic:
# Rows = 5
# In each row, spaces = row number
# In each row, stars = 5 - row number