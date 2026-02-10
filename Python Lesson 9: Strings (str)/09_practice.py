# Reverse a string using loop

s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

print("Reversed:", rev)