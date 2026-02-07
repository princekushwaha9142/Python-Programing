# Count even numbers
count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count += 1

print(count)

# Sum until user enters 0
total = 0

while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    total += num

print("Sum:", total)