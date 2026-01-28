# We convert one data type to another.

# String → Integer
age = int(input("Enter your age: "))
print(age)
print(type(age))

# String → Float
height = float(input("Enter your height: "))

# Any → String
age = 20
print("Age is " + str(age))

# Common Type Casting Errors

# This will crash:

age = int("abc")

# This will crash:

age = int("20.5")


# Correct:

age = float("20.5")

