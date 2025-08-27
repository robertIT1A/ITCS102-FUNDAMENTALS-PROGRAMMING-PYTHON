username = "Junior"
password = "Good_B0y"

import getpass
while True: #To repeat the username until it's correct
    name = input("Enter your username: ")
    if name == username:
        print("Username Identified\n")
        break #Exit the loop
    else:
        print("Incorrect Username")
        print("Please Try Again\n")

password1 = input("Enter your password:")
if password1 == password:
    print("Access Complete")
else:
    print("Access Denied")

