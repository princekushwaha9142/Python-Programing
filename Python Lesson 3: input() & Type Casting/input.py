# Basic syntax:

input()

# Example:

name = input("Enter your name: ")
print("Hello", name)

# What’s happening?
# Program pauses
# User types something
# Python stores it in name

# input() ALWAYS returns a STRING (str)

# Example:

age = input("Enter your age: ")
print(type(age))

# Even if you type 20, Python sees it as:
# <class 'str'>
