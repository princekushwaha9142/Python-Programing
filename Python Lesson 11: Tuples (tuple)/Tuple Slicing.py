t = (10, 20, 30, 40, 50)

t[1:4]  # Output: (20, 30, 40)
t[:3]   # Output: (10, 20, 30)
t[2:]   # Output: (30, 40, 50)
t[-3:-1] # Output: (30, 40)



# Tuples are IMMUTABLE 

# NOT allowed:

a = (10, 20, 30)
a[0] = 99    # ERROR  

# Python error:

# TypeError: 'tuple' object does not support item assignment