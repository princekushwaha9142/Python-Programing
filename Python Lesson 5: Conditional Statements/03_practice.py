username = input("Enter a username: ")
password = int(input("Enter a Password: "))
if username == "admin" and password == 1234:
    print("Access Granted")
elif username == "admin" and password != 1234:
    print("Incorrect Password")
else:
    print("Unknown User")

