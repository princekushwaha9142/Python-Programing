# convert tuple to list, modify it, and convert back to tuple
t = (10, 20, 30, 40, 50)
l = list(t)
l[2] = 35
t = tuple(l)
print(t)  # Output: (10, 20, 35, 40, 50)