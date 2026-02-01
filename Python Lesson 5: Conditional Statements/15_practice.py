salary = float(input("Enter your salary: "))
if salary < 300000:
    tax  = 0
elif salary < 700000:
    tax = salary * 0.10
else:
    tax = salary * 0.20
print("Tax to be paid: ₹", tax)
