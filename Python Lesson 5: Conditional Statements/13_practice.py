a = int(input("Enter a number: "))
if a % 3 == 0 and a % 5 == 0:
    print("Divisible by both 3 and 5")
elif a % 3 == 0:
    print("Divisible by 3")
elif a % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")