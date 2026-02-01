unit = int(input("Enter unit consumed: "))
bill = 0
if unit <= 100:
    bill = 0
elif unit <= 200:
    bill = (unit - 100) * 5
else:
    bill = 100 * 5 + (unit - 200) * 10

print("Total Electricity Bill: ₹", bill)
