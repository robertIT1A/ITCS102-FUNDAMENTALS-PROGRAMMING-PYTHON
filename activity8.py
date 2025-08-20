balance = 1000
amount = 0

amount = int(input("Enter the amount to withdraw:"))
print(balance >= amount)
if balance >= amount:
    print("Here's you", amount, "Thank you!")
    ramaining = balance - amount
    print("Your remaining balance is", ramaining)
elif balance <= amount:
    print("You have not enough balance, please try again!")
    print("Your balance is only", balance)