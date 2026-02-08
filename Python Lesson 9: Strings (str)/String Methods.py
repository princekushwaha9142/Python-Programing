# Case methods

s = "pYtHoN"

print(s.lower())   # python
print(s.upper())   # PYTHON
print(s.title())   # Python

# Remove spaces

s = "  hello  "
print(s.strip())

# Replace

s = "I like Java"
print(s.replace("Java", "Python"))

# Split 

s = "Python is awesome"
print(s.split())

# Length

print(len("Python"))  # 6

# Count

s = "banana"
print(s.count("a"))  # 3

# Starts / Ends

s = "python.py"
print(s.startswith("py"))
print(s.endswith(".py"))