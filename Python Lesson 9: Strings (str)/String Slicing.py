s = "Python Programming"

print(s[0:6])     # Python
print(s[7:18])    # Programming
print(s[:6])      # Python
print(s[7:])      # Programming
print(s[::2])     # Pto rgamn

# Format:
# string[start : end : step]


# Strings are IMMUTABLE 

#  Wrong:

s = "hello"
s[0] = "H"   # ERROR

# Correct:

s = "hello"
s = "H" + s[1:]
print(s)