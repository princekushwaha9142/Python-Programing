m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))
average = (m1 + m2 + m3) / 3

if m1 < 33 or m2 < 33 or m3 < 33:
    print("Fail")
elif average >= 75:
    print("Distinction")
elif average >= 60:
    print("First class")
elif average >= 40:
    print("Pass")
else:
    print("Fail")