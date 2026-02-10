# Check palindrome

s = input("Enter a string: ").lower()

rev = s[::-1]

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
