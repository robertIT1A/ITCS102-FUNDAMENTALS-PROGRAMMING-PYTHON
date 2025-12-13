def act8():
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

def code8():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""balance = 1000
amount = 0

amount = int(input("Enter the amount to withdraw:"))
print(balance >= amount)
if balance >= amount:
    print("Here's you", amount, "Thank you!")
    ramaining = balance - amount
    print("Your remaining balance is", ramaining)
elif balance <= amount:
    print("You have not enough balance, please try again!")
    print("Your balance is only", balance)""")
    print("\n------------------------------------")


#Loyalty card discount
#If the user have a loyalty card, loyalty card discount must be applied
#30% discount for loyalty card, if no loyalty card no discount
def act10():
    name = input("Enter your name: ")
    Loyalty_card = input("Do you have a loyalty card (Yes / No): ")
    amount = eval(input("Amount of the item/s: "))

    if Loyalty_card.lower() == "yes": 
        discount = amount * .3 
        new_amount = amount - discount
        print("Good day", name.title(),"\n Original Price:", amount, "\n Cash Payment Discount:", discount, "\n Grand Total:", new_amount) 
        print("Thank you for coming!")
        print("Have a nice day!")
    else:
        print("Good day", name.title(), "sorry your not eligible for discount.", "\nOriginal Price:", amount)
        print("Thank you for coming!")
        print("Have a nice day!")

def code10():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""name = input("Enter your name: ")
Loyalty_card = input("Do you have a loyalty card (Yes / No): ")
amount = eval(input("Amount of the item/s: "))

if Loyalty_card.lower() == "yes": 
    discount = amount * .3 
    new_amount = amount - discount
    print("Good day", name.title(),"\n Original Price:", amount, "\n Cash Payment Discount:", discount, "\n Grand Total:", new_amount) 
    print("Thank you for coming!")
    print("Have a nice day!")
else:
    print("Good day", name.title(), "sorry your not eligible for discount.", "\nOriginal Price:", amount)
    print("Thank you for coming!")
    print("Have a nice day!")""")
    print("\n------------------------------------")

#Identify the whole number
#Odd or Even
#Possitive or Negative
def act11():
    num = int(input("Enter a number: "))

    if num >= 1 and num % 2 == 0:
        print("Possitive and Even")

    elif num >= 1 and num % 2 != 0:
        print("Possitive and Odd")

    elif num <= -1 and num % 2 == 0:
        print("Negative and Even")

    elif num % 2 != 0 and num <= -1:
        print("Negative and Odd")

    else:
        print("Zero")


def code11():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""num = int(input("Enter a number: "))

if num >= 1 and num % 2 == 0:
    print("Possitive and Even")

elif num >= 1 and num % 2 != 0:
    print("Possitive and Odd")

elif num <= -1 and num % 2 == 0:
    print("Negative and Even")

elif num % 2 != 0 and num <= -1:
    print("Negative and Odd")

else:
    print("Zero")""")
    print("\n------------------------------------")