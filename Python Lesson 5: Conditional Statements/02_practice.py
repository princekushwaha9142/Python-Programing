marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks < 89:
    print("Grade: B")
elif 60 <= marks < 74:
    print("Grade: C")
else:
    print("Grade: Fail")