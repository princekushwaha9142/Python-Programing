a =  int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
elif c >= a and c >= b:
    print("Largest number is:", c)
else:
    print("All numbers are equal")