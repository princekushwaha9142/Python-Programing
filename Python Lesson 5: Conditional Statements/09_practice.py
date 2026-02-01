marks = int(input("Enter marks (0–100): "))

is_valid = 0 <= marks <= 100
print("Valid marks:", is_valid)

if marks >= 40:
    print("Pass")
else:
    print("Fail")
