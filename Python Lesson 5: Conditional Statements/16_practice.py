time = int(input("Enter time in 24-hour format (0-23): "))
if 5 <= time <= 11:
    print("Good Morning")
elif 12 <= time <= 16:
    print("Good Afternoon")
elif 17 <= time <= 20:
    print("Good Evening")
elif 21 <= time <= 23 or 0 <= time <= 4:
    print("Good Night")
else:
    print("Invalid time")
